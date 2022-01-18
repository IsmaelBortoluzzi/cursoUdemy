from string import Template
from datetime import datetime

with open("mandar_email.html", "r") as html:
    template = Template(html.read())
    corpo_msg = template.substitute(nome='ismael', data=datetime.now().strftime('%d/%m/%Y'))

print(corpo_msg)