# Main funksjon i Python

Dere skal benytte dere av en såkalt main()-funksjon i Python. Dette er en konvensjon som ofte brukes i Python, der man legger all koden sin i funksjoner som kan kalles fra en egen main()-funksjon. Main er slik den eneste funksjonen som skal kjøres av brukeren (når man kjører Python-filen). Dvs. main må inneholde en while loop, som gjør at brukeren kan gjøre gjentatte funksjoner uten å måtte starte programmet på nytt. Her er det også viktig at main-funksjonen/while-loopen kan stoppes og programmet kan avbrytes.

## Pseudokode:

```python
# NB! Dette er pseudokode og ikke python kode!!
main():
	while true:
		user_input = get user_input # bruker velger hva hen vil gjøre
		if user_input == logg_inn:
			run login()  # kjører log-in()-funksjonen
		else if user_input == do_stuff:
			run doStuff() # kjører do-stuff()-funksjonen
		else if user_input() == exit:
			run exit()  # stopp while-loopen og programmet avsluttes
```

For å kjøre `main()` funksjonen legger du kallet på slutten av koden din. Her kan du velge å gjøre en spesiell “if-setning” som gjør at vi kan endre/modifisere kallet slik vi ønsker. Dette gjør vi ved å skrive:

```python
# Dette er Python kode dere godt kan bruke
if __name__ == "__main__":
   main()
```

I koden over endrer `__name__` seg til hvordan vi kaller programmet. Kjører vi Python-filen gjennom kommandolinjen eller med `python -m` vil `__name__` være det samme som `__main__`. Dette kan være smart hvis vi skulle ønske å kjøre andre moduler i stedet for main. Mer info [her](https://realpython.com/python-main-function/).
