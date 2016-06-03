import sys

class Reporter(object):
    '''Collect and report errors.'''

    def __init__(self, args):
        '''Constructor.'''

        super(Reporter, self).__init__()
        self.messages = []


    def check_field(self, filename, name, values, key, expected):
        '''Check that a dictionary has an expected value.'''

        if key not in values:
            self.add('{0} does not contain {1} in {2}',
                     name, key, filename)
        elif values[key] != expected:
            self.add('{0} {1} is {2} not {3} in {4}',
                     name, key, values[key], expected, filename)


    def check(self, condition, fmt, *args):
        '''Append error if condition not met.'''

        if not condition:
            self.add(fmt, *args)


    def add(self, fmt, *args):
        '''Append error unilaterally.'''

        self.messages.append(fmt.format(*args))


    def report(self, stream=sys.stdout):
        '''Report all messages.'''

        if not self.messages:
            return
        for m in self.messages:
            print(m, file=stream)
