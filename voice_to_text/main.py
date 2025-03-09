'''
This class is responsible for invoking the appropriate
strategy for processing audio data into text.
- strategy is an instance of a class that implements the process_data() method
- process_data() method is overwritten in other classes
'''
class Transcriber:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def process_data(self, *args, **kwargs):
        return self.strategy.process_data(*args, **kwargs)

def main():
    # the idea is to get a type of user input
    # and instantiate the appropriate strategy
    # for processing
    ...
