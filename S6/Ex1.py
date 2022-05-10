# 4. Scrieti o functie care returneaza volumul unui cub in litri. Aceasta va primi
# un singur agument reprezentand muchia cubului in metri.

# 6. Scrie o functie care converteste litrii in metri cubi.

def cube_volume(edge):
    """Calculate cube volume in liters."""
    # 1 m3 = 1000 litri
    return edge ** 3 * 1000

def convert_to_m3(liters):
    """Convert liters in m3."""
    return liters / 1000

print("Volumul cubului: ", convert_to_m3(cube_volume(18)) ,"m3")