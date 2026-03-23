from ll import Node, LinkedList

canciones = [
	("Maldita costumbre", "Morat", "Balas Perdidas"),
	("Cómo te atreves", "Morat", "Sobre el amor y sus efectos secundarios"),
	("A dónde vamos", "Morat", "A dónde vamos"),
	("Besos en guerra", "Morat", "Sobre el amor y sus efectos secundarios"),
	("Cuando nadie ve", "Morat", "Balas Perdidas"),
	("Yo contigo, tú conmigo", "Morat", "Yo contigo, tú conmigo"),
	("No se va", "Morat", "Si ayer fuera hoy"),
	("París", "Morat", "Si ayer fuera hoy"),
	("Date la vuelta", "Luis Fonsi", "Vida"),
	("Enamórate de alguien más", "Morat", "Balas Perdidas"),
	("Perfect", "Ed Sheeran", "Divide"),
	("Shape of You", "Ed Sheeran", "Divide"),
	("Photograph", "Ed Sheeran", "Multiply"),
	("Thinking Out Loud", "Ed Sheeran", "Multiply"),
	("The A Team", "Ed Sheeran", "Plus"),
	("Castle on the Hill", "Ed Sheeran", "Divide"),
	("Shivers", "Ed Sheeran", "Equals"),
	("Bad Habits", "Ed Sheeran", "Equals"),
	("Galway Girl", "Ed Sheeran", "Divide"),
	("Afterglow", "Ed Sheeran", "Afterglow"),
	("Viva la Vida", "Coldplay", "Viva la Vida"),
	("Yellow", "Coldplay", "Parachutes"),
	("The Scientist", "Coldplay", "A Rush of Blood to the Head"),
	("Fix You", "Coldplay", "X&Y"),
	("Paradise", "Coldplay", "Mylo Xyloto"),
	("A Sky Full of Stars", "Coldplay", "Ghost Stories"),
	("Adventure of a Lifetime", "Coldplay", "A Head Full of Dreams"),
	("Clocks", "Coldplay", "A Rush of Blood to the Head"),
	("Sparks", "Coldplay", "Parachutes"),
	("Hymn for the Weekend", "Coldplay", "A Head Full of Dreams"),
	("Blinding Lights", "The Weeknd", "After Hours"),
	("Save Your Tears", "The Weeknd", "After Hours"),
	("Starboy", "The Weeknd", "Starboy"),
	("Die For You", "The Weeknd", "Starboy"),
	("The Hills", "The Weeknd", "Beauty Behind the Madness"),
	("Can't Feel My Face", "The Weeknd", "Beauty Behind the Madness"),
	("Earned It", "The Weeknd", "Beauty Behind the Madness"),
	("Call Out My Name", "The Weeknd", "My Dear Melancholy"),
	("I Feel It Coming", "The Weeknd", "Starboy"),
	("In Your Eyes", "The Weeknd", "After Hours"),
	("As It Was", "Harry Styles", "Harry's House"),
	("Watermelon Sugar", "Harry Styles", "Fine Line"),
	("Adore You", "Harry Styles", "Fine Line"),
	("Sign of the Times", "Harry Styles", "Harry Styles"),
	("Late Night Talking", "Harry Styles", "Harry's House"),
	("Golden", "Harry Styles", "Fine Line"),
	("Kiwi", "Harry Styles", "Harry Styles"),
	("Falling", "Harry Styles", "Fine Line"),
	("Satellite", "Harry Styles", "Harry's House"),
	("Music for a Sushi Restaurant", "Harry Styles", "Harry's House"),
]

playlist = LinkedList()

for nombre, artista, album in canciones:
	playlist.insert_at_end(Node(nombre, artista, album))

if playlist.start is None:
	print("La playlist esta vacia.")
else:
	actual = playlist.start
	print(f"Total de canciones cargadas: {len(playlist)}")

	while True:
		print("\nReproduciendo ahora:")
		print(f"- Cancion: {actual.data['nombre']}")
		print(f"- Artista: {actual.data['artista']}")
		print(f"- Album: {actual.data['album']}")

		print("\nOpciones: [n] siguiente | [p] anterior | [q] salir")
		opcion = input("Selecciona una opcion: ").strip().lower()

		if opcion == "n":
			if actual.next is None:
				print("Ya estas en la ultima cancion.")
			else:
				actual = actual.next
		elif opcion == "p":
			if actual.prev is None:
				print("Ya estas en la primera cancion.")
			else:
				actual = actual.prev
		elif opcion == "q":
			print("Saliendo de la playlist.")
			break
		else:
			print("Opcion invalida. Usa n, p o q.")