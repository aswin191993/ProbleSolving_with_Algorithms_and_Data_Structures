import queues
import random
class printer:
	def __init__(self,ppm):
		self.p_rate = ppm
		self.t_rem = 0
		self.current_t = None

	def tick(self):
		if self.current_t != None:
			self.t_rem = self.t_rem - 1
			if self.t_rem <= 0:
				self.current_t = None
	def busy(self):
		if self.current_t != None:
			return True
		else:
			return False
				
	def start_next(self,new_task):
		task=Task()
		self.current_t = new_task
		self.t_rem = new_task.task.get_pages() * 60 / self.page_rate

class Task:
	def __init__(self, time):
		self.timestamp = time
		self.pages = random.randrange(1, 21)
	
	def get_stamp(self):
		return self.timestamp
	
	def get_pages(self):
		return self.pages
	
	def wait_time(self, current_time):
		return current_time - self.timestamp
		


q=printer(4)
#print q.start_next(12)
#q.enque("asd")
#q.enque("uio")
#q.enque("bnnm")
#print q.deque()
#print q.is_empty()
#q.prnt()
