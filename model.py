#import necessary modules from python
from mesa import Model
from agent import ResidentAgent
from agent import NurseAgent
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import mesa

#Defining the model 
class CareHomeModel(Model):
    """A model with some number of agents."""

    def __init__(self, n_residents, n_nurses, width, height):
        self.num_residents = n_residents
        self.num_nurses = n_nurses
        self.headings = {(1, 0), (0, 1), (-1, 0), (0, -1)}
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True
        # Create agents
        #Resident Agent
        for t in range(self.num_residents):
            #pos = (x, y)
            heading = (1, 0)
            k = ResidentAgent(t,self)
            self.schedule.add(k)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(k, (x, 45))
        
        
        #Nurse Agent
        for r in range(self.num_residents+1, self.num_nurses+self.num_residents+1):
            pos = (x, y)
            heading = (1, 0)
            f = NurseAgent(r,self)
            self.schedule.add(f)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(f, (25,2))
            
    #Adding all the agents to schedule       
    def step(self):
        self.schedule.step()