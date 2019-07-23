import openpyxl
from app.models import Delivery


wb = openpyxl.load_workbook('list.xlsx')

ws = wb.active

for r in ws.rows:
    name = r[0].value
    housetype = r[1].value
    news_type = r[2].value
    image = r[3].value
    etc = r[4].value
    item = Delivery(name=name,housetype=housetype,kind_of_news=news_type,images=image,etc=etc)
    item.save()
    print(item,'saved')
    
