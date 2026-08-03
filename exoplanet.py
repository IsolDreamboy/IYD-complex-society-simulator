
import random


class ExoplanetK2_18b:
     def __init__(self):
        self.star= "Red Dwarf"
        self.rotation=True
        self.gravity= "High(SuperTerra 12,43 m/s² ou 1,27 g)"
        self.ocean_pressure="Extreme(10 to thousands of bars)"
        self.atmosphere="H, C , O , S , He , N"


class primitive_ancestor:
    def __init__(self,density,flexibility):
        self.metabolism=random.choice(["methane chemosynthesis", "Photosynthesis","Chemolithotrophy","Cellular Respiration", "Hydrogen Oxidation","Methanogenesis", "Hyperthermophiles"])
        self.randomdensity=random.randint(1,100)
        self.randomflexibility=random.randint(1,100)


    def genes(self,flexibility,density):
        if flexibility <50 and density <50:
            print("Your genes could not go any further.")
            return False

            print("Your genes can go any further.")

            successeful_flex_gen= flexibility + random.randint(-5, 5)
            successeful_density_gen = density + random.randint(-5, 5)

            succeeded_gen= primitive_ancestor(successeful_density_gen, successeful_flex_gen)
        

if __name__ == "__main__":
    first_ancestral = primitive_ancestor(40, 60)
    print("Metabolismo sorteado:", first_ancestral.metabolism)
    first_ancestral.genes(40, 60)

