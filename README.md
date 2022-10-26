# friends-birthday-bot
this is a simple bot to don't forget your friends birthday )

##### bul botqa dostlarin'iz ara tura kirip dostlardin' tuwilg'an kunlerin ko'rip, jasliqti eslep, harturli qiziqli waqiyalar ko'z aldine keliwi mumkin. Eger rastanda usinday bo'lsa paydasi tiygennen quwanishliman

Bul programmani iske tusiriw ushin to'mendegi ketpe ketlikti qo'llawin'iz kerek. albette bul programmanin' codelarin o'zgertirib ja'nede ko'plegen funktsiyalar qo'ssan'iz bo'ladi

```
pythondi ornatiw
doslarin'izdin' tuwilg'an sanelerin bazag'a kiritiw 
suwretlerdi kerekli papkalarg'a saqlaw
usinis etetin qosiqlarin'izdi kerekli papkag'a saqlaw(keminde birew)
```
- pythondi ornatiw ushin(linux distributorlar ushin)
>$ sudo apt install python3 \
>$ sudo apt-get update

- windows paydalaniwshilar ushin
[python3](python.org/downloads/) tan juklep ala alasiz MacOs ushinda usi jerde bar

- Hamde botti iske ushin tusiriw aldin pip di keyin telegram bot kutipxanasin qosiwingiz talap etiledi
> $ python -m pip install --upgrade pip
> $ pip install python-telegram-bot --upgrade

- Dostlarin'izding tuwilg'an sanelerin bazag'a kiritiw oni [db-Browser-Sqlite](https://sqlitebrowser.org/dl/) arqali toldrip shiqsangiz bo'ladi
<table>
<tr>
<th>id</th>
<th>name</th>
<th>surname</th>
<th>year</th>
<th>month</th>
<th>day</th>
</tr>
misali
<tr>
<td>1</td>
<td>Sardor</td>
<td>Matniyazov</td>
<td>2003</td>
<td>01</td>
<td>22</td>
</tr>
</table>

- kiyin usi id lardi bilgen halda images papkag'a suwretlerdi id bo'yincha saqlaw. (misali: 1.jpg(bul tobedegi misaldag'i Sardording suwreti))


# Run beriw
Botti iske tusiriw ushin main.py fayldi iske tusiriwingiz kerek bo'ladi
> python3 main.py 
Note: albette bul jerde glavniy papka ishinde main.py turg'an jerde bo'liw kerek
pycharm uqsag'an IDE larda tursan'iz bul angsat keshedi
