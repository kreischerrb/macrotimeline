#!/usr/bin/env python3
"""Gera dados/taco.json a partir do PDF oficial da Tabela TACO 4ª edição (NEPA/Unicamp).

Uso (uma vez, no computador; o app não precisa deste script para funcionar):
  pdftotext -layout taco_4_edicao_ampliada_e_revisada.pdf taco.txt
  python3 ferramentas/gerar_taco.py taco.txt dados/taco.json

Lê só a Tabela 1 (composição centesimal por 100 g). Regras:
  - "Tr" (traço)                       -> 0
  - "NA", "*" (em reavaliação) ou vazio -> null ("sem dado" no app)
Nenhum número é digitado à mão: tudo sai do texto do PDF.
"""
import json, re, sys
from statistics import median

# Colunas da parte centesimal da Tabela 1, na ordem do PDF
COLS = ['umidade', 'kcal', 'kj', 'prot', 'gord', 'colesterol', 'carb', 'fibra', 'cinzas', 'calcio', 'magnesio']
TOK = r'(?:\d+(?:,\d+)?|NA|Tr|\*)'
ROW = re.compile(r'^\s*(\d{1,3})\s{2,}(.+?)\s{2,}(' + TOK + r'(?:\s+' + TOK + r')*)\s*$')


def valor(t):
    if t is None or t in ('NA', '*'):
        return None
    if t == 'Tr':
        return 0
    v = float(t.replace(',', '.'))
    return int(v) if v.is_integer() and ',' not in t else v


def main(src, dst):
    pages = open(src, encoding='utf-8').read().split('\f')
    foods, group = {}, None
    for page in pages:
        if 'Tabela 1' not in page or 'Umidade' not in page:
            continue
        rows = []
        started = False
        for line in page.split('\n'):
            if '(kcal)' in line:
                started = True
                continue
            if not started or not line.strip() or re.match(r'^\s*\d+\s*$', line):
                continue
            m = ROW.match(line)
            if m:
                # guarda o texto de cada célula e a posição (coluna de caracteres) onde ela termina
                start = m.start(3)
                cells = [(x.group(), start + x.end()) for x in re.finditer(r'\S+', m.group(3))]
                nome = re.sub(r'\s+\d$', '', m.group(2).strip())  # tira marca de nota de rodapé
                rows.append((int(m.group(1)), nome, group, cells))
            elif not line.startswith(' ' * 5) and line.strip()[0].isupper():
                group = line.strip()
            else:
                raise SystemExit('Linha não reconhecida: ' + line)
        # posição de cada coluna nesta página, tirada das linhas completas
        full = [r[3] for r in rows if len(r[3]) == len(COLS)]
        edges = [median(c[i][1] for c in full) for i in range(len(COLS))]
        for n, nome, grp, cells in rows:
            vals = dict.fromkeys(COLS)
            if len(cells) == len(COLS):
                for col, (t, _) in zip(COLS, cells):
                    vals[col] = t
            else:  # linha com células vazias: cada valor vai para a coluna mais próxima
                for t, end in cells:
                    i = min(range(len(COLS)), key=lambda k: abs(edges[k] - end))
                    if vals[COLS[i]] is not None:
                        raise SystemExit('Duas células na mesma coluna, alimento %d' % n)
                    vals[COLS[i]] = t
            foods[n] = {'n': n, 'nome': nome, 'grupo': grp,
                        'kcal': valor(vals['kcal']), 'prot': valor(vals['prot']),
                        'carb': valor(vals['carb']), 'gord': valor(vals['gord']),
                        'fibra': valor(vals['fibra'])}
    nums = sorted(foods)
    if nums != list(range(1, len(nums) + 1)):
        raise SystemExit('Faltam alimentos na numeração')
    out = {
        'fonte': 'Tabela Brasileira de Composição de Alimentos – TACO, 4ª edição revisada e ampliada. NEPA/Unicamp, 2011. Tabela 1.',
        'unidade': 'por 100 g de parte comestível; kcal; demais em gramas; null = sem dado (NA ou em reavaliação na TACO); Tr = 0',
        'alimentos': [foods[n] for n in nums],
    }
    with open(dst, 'w', encoding='utf-8') as f:
        f.write('{\n')
        for k in ('fonte', 'unidade'):
            f.write('  %s: %s,\n' % (json.dumps(k), json.dumps(out[k], ensure_ascii=False)))
        f.write('  "alimentos": [\n')
        f.write(',\n'.join('    ' + json.dumps(a, ensure_ascii=False) for a in out['alimentos']))
        f.write('\n  ]\n}\n')
    print(len(nums), 'alimentos gravados em', dst)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
