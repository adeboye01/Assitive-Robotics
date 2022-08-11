#import necessary modules from python
import mesa
from mesa import Agent
#Defining the Resident Agent
class ResidentAgent(mesa.Agent):
    """Resident agent."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.residence = 1
        
    def step(self) -> None:                                                                                                             
        self.move()   
        if self.residence > 0:
            self.walk()
       
    def walk(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = self.random.choice(cellmates)
            other.residence += 1
            self.residence -= 1
      
    def move(self):
        possible_steps = [(self.pos[0],self.pos[1]),(self.pos[0]-1,self.pos[1]), (self.pos[0],self.pos[1]-1)]
        
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    
    
 #Defining the nurse agent   
class NurseAgent(mesa.Agent):
   """Nurse agent."""

   def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.nurse = 1
        
       
