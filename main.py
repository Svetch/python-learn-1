from tasks import task1, task2, Planet, PlanetEncoder

task1()
task2()


planets: list[Planet] = []
with open("egitestek.txt", "r") as f:
    for line in f:
        planets.append(Planet(line))

print("3.1. feladat: " +
      str(len(planets)) +
      " db égitest van a fájlban.")

print("3.2. feladat: " +
      str(len([planet for planet in planets if planet.location == "Nap"])) +
      " égitest KEring a Nap körül.")

print("3.3. feladat: a " +
      sorted(planets, key=lambda planet: planet.distance, reverse=True)[0].name +
      " van a legközelebb az égitesthez, mely körül kering")

print("3.4. feladat: A Földével ellentétes keringési irányú égitestek:\n" +
      ''.join("\t\t- "+p + "\n" for p in [planet.name for planet in planets if planet.direction == 0]))

planerName = input("3.5. feladat: írja be a keresett égitest nevét:")

planet = next(
    (planet for planet in planets if planet.name == planerName), None)

if planet is not None:
    print("\t\t a(z)" +
          planet.name +
          " szerepel a listában\n\t\t felfedezője: " +
          planet.explorer + "\n\t\t felfedezés éve: " +
          str(planet.exploredYear))

else:
    print("\t\t a(z)" +
          planerName +
          " nem szerepel a listában")
