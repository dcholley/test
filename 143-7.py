import matplotlib.pyplot as plt
import numpy as np
import PIL

def make_mask(rows, columns, stripe_width):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(rows):
        for column in range(columns):
            if row % 5 == 0: 
                image[row][column] = [200, 0, 200, 255]
 
            else:
                image[row][column] = [0, 255, 0, 0] 
                if column % 3 == 0: 
                    image[row][column] = [100, 0, 100, 255] 
                else:
                    image[row][column] = [0, 255, 0, 0] 
    return image
    
if __name__ == "__main__":
    image = make_mask(100,100,20)
    
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    fig.show()            
              
