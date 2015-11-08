# ISPUAPI DOCUMENTATION

- about

ISPUAPI (ISPU+API)
Appliaction Programming Interface
for PM10 data retreival on current location in Indonesia.
it is defaultly retreive PM10 data for Pekanbaru.
data retreival for other locations is still under development
some functions still buggy or the data is not entirely valid except
for Pekanbaru.

- installation
** `$ sudo pip -r requirements.txt`
** `$ git clone https://github.com/vickydasta/ispuapi`
** `$ pip install -e api`
** `$ python ispuapi.py`

a matplotlib window should appears after the scrapper fetch
the needed data from the source and plot the data

- functions
```
>>> import ispuapi
>>> site = 'somesite'
>>> [in]: data = ispuapi.getdataispu(site)
>>> [out]: {'bmkg':data_html}
>>> [in]: ispuapi.aqi('pku')
>>> [out]: <some values>
```

- author

vickydasta (Vicky Vernando Dasta)
