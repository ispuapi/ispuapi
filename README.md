# Tentang ISPUAPI Python

## ISPUAPI - (ISPU + API)
### ISPU -> (Indeks Standar Polusi Udara) + API (Application Programming Interface)

```
ispuapi adalah API Python untuk information retreival terhadap data terkait ISPU (PM10) di kota Pekanbaru.
```

# Instalasi

- not yet written :P

# HOWTO

- howto using ispuapi

```
>> import ispuapi.ispuapi
>> pku = ispuapi.aqi('pku') # dapatkan data air quality indeks berdasarkan kode kota
>> import matplotlib.pyplot as plt # modul plotting
>> plt.xlabel('Waktu')
>> plt.ylabel('Tingkat PM10')
>> plt.plot(pku)
>> plt.show()
```

- howto connect to mysql

```
>> import enginx
>> 

```

# Author

- Vicky Vernando Dasta
