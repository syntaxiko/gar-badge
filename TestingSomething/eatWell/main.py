''' 
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

'''
    Tomorrow Was the Day to Begin

'''
def test1():
    dOne = {
        'key':'value',
        'key2':'value'
        }
    
    dTwo = dOne.copy()
    
    print dOne == dTwo
    
    dOne.clear()
    print dOne
    
    print dOne.clear()
    print type(dOne.clear())

class AnyClass(object):
    '''Class docstring'''
    
    def __init__(self,arg1,arg2):
        '''method docstring'''
        self.arg1 = arg1
        self.arg2 = arg2
        
    def printargs(self):
        '''method docstring'''
        print self.arg1
        print self.arg2

def main():
    test1()
    instance = AnyClass('string1','string2')
    instance.printargs()
    

main()