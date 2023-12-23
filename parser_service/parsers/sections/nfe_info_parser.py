import re
from collections import namedtuple



LinePattern = namedtuple('LinePattern', ['content_key', 'line_offset'])


class NfeInfoParser:

    @staticmethod
    def parse(data):
        reference_map = {
            'chave de acesso:': LinePattern("access_key", 1),
            'Vencimento': LinePattern("due_date", 4),
            'Nº DO CLIENTE': LinePattern("client_number", 2),
            'Nº DA INSTALAÇÃO': LinePattern("installation_number", 2),
            'Total a pagar': LinePattern('total_amount', 4),
            '(Data de emissão:) (.*)$': LinePattern('issue_date', -1),
            'Referente a': LinePattern('reference_month', 3)
        }
        nf_code = re.compile(r'(\d{11}-\d ){3}')
        content = {}
        for i, line in enumerate(data):
            if nf_code.search(line):
                content["nf_code"] = line
                continue
            for text, pattern in reference_map.items():
                compiled_pattern = re.compile(text)
                match = compiled_pattern.search(line)
                if match:
                    content[pattern.content_key] = (
                        match.group(2) if pattern.line_offset == -1 else data[i + pattern.line_offset])
        return {"name": "nfe_infos", "content": content}
