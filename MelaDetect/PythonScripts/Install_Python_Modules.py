import pip

def install(package):
    pip.main(['install', package])

if __name__ == '__main__':
   install('tensorflow')
   install('Flask')
   install('opencv-python')
   install('os-win')
	
