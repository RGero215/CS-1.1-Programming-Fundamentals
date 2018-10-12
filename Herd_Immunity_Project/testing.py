import unittest
import virus
import person
import simulation

class Testing(unittest.TestCase):
    virus = virus.Virus("Ebola", 0.70, 0.25)
    person1 = person.Person(1, False, virus)
    person2 = person.Person(2, True, False)
    person3 = person.Person(3, False, False)
    person4 = person.Person(4, False, None)
    person5 = person.Person(5, True, False)
    simulation = simulation.Simulation(100, 0.90, "Ebola", 0.70, 0.25, 10)

    def test_virus(self):
        self.assertEqual(self.virus.name, "Ebola")
        self.assertEqual(self.virus.mortality_rate, 0.70)
        self.assertEqual(self.virus.basic_repro_num, 0.25)

    def test_person(self):
        self.person1.infected = self.virus
        self.person1.is_vaccinated = False
        self.assertEqual(self.person1.infected, self.virus)
        self.assertEqual(self.person1.is_vaccinated, False )
        self.assertEqual(self.person1._id, 1)
        self.assertEqual(self.person2.infected, False)
        self.assertEqual(self.person2.is_vaccinated, True )
        self.assertEqual(self.person2._id, 2)
        self.assertEqual(self.person3.infected, False)
        self.assertEqual(self.person3.is_vaccinated, False )
        self.assertEqual(self.person3._id, 3)

    
    def test_did_survive_infection(self):
        self.assertEqual(self.person1.did_survive_infection(), False)
        self.assertEqual(self.person2.did_survive_infection(), 0)
        self.assertEqual(self.person3.did_survive_infection(), 0)

    def test_create_population(self):
        self.assertEqual(self.simulation._create_population(self.simulation.initial_infected), self.simulation.population)
        
    # def test_simulation_should_continue(self):
    #     self.assertEqual(self.simulation._simulation_should_continue(), True)
    #     self.person1.is_alive = False
    #     self.person2.is_alive = False
    #     self.person3.is_alive = False
    #     population = [self.person1, self.person2, self.person3]
    #     self.simulation.population = population
    #     self.assertEqual(self.simulation._simulation_should_continue(), False)

    # def test_time_step(self):
    #     self.assertEqual(self.simulation.time_step(), 100)

    # def test_run(self):
    #     self.assertEqual(self.simulation.run(), 10)

    def test_interaction(self):
        self.person1 = person.Person(1, False, self.virus)
        self.person1.is_alive = True
        self.person5.is_alive = True
        self.assertEqual(self.simulation.interaction(self.person1, self.person4), 0)
        self.assertEqual(self.simulation.interaction(self.person1, self.person1), 0)
        self.person1.is_alive = True
        self.assertEqual(self.simulation.interaction(self.person1, self.person5), 1)
    
    def test_infect_newly_infected(self):
        self.person6 = person.Person(6, False, self.virus)
        self.person7 = person.Person(7, False, False)
        self.simulation.population = [self.person6, self.person7]
        self.simulation.newly_infected = [self.person6, self.person7]
        self.assertEqual(self.simulation._infect_newly_infected(), True)



if __name__ == "__main__":
    unittest.main()
        