from PIL import Image
def main():
    
    image1 = Image.open("C:/Users/KAVYA/Desktop/7th sem/Assignment_1/QUESTION_1/picture1.jpg")
    image2 = Image.open('C:/Users/KAVYA/Desktop/7th sem/Assignment_1/QUESTION_1/picture2.jpg')
    image3 = Image.open('C:/Users/KAVYA/Desktop/7th sem/Assignment_1/QUESTION_1/picture3.jpg')
    image4 = Image.open('C:/Users/KAVYA/Desktop/7th sem/Assignment_1/QUESTION_1/picture4.jpg')
    image5 = Image.open('C:/Users/KAVYA/Desktop/7th sem/Assignment_1/QUESTION_1/picture5.jpg')

   
    image1.convert('RGB')
    image2.convert('RGB')
    image3.convert('RGB')
    image4.convert('RGB')
    image5.convert('RGB')
    imageList = [image2, image3, image4, image5]

    
    fileName = 'C:/Users/KAVYA/Desktop/7th sem/Assignment_1/QUESTION_1/Pictures.pdf'
    image1.save(fileName, save_all=True, append_images=imageList)
    print('Done')


if __name__ == '__main__':
    main()
