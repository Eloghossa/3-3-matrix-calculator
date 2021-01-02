#Lines of code 



print("OPERATIONS MENU\n  1. Addition\n  2. Substraction\n  3. Multiplication\n  4. Exit")
Op = int(input("Enter option number: "))
if Op==4:
	exit()
elif Op > 4:
	print("Enter the right option")
	exit()
Matrix_1_row_1 = input("Enter values for matrix 1 row 1 separated by commas: ")
Mat11 = Matrix_1_row_1.split(",")
Mat11 = list(map(int, Mat11)) 
Matrix_1_row_2 = input("Enter values for matrix 1 row 2 separated by commas: ")
Mat12 = Matrix_1_row_2.split(",")
Mat12 = list(map(int, Mat12)) 
Matrix_1_row_3 = input("Enter values for matrix 1 row 3 separated by commas: ")
Mat13 = Matrix_1_row_3.split(",")
Mat13 = list(map(int, Mat13)) 
Matrix_2_row_1 = input("Enter values for matrix 2 row 1 separated by commas: ")
Mat21= Matrix_2_row_1.split(",")
Mat21 = list(map(int, Mat21)) 
Matrix_2_row_2 = input("Enter values for matrix 2 row 2 separated by commas: ")
Mat22 = Matrix_2_row_2.split(",")
Mat22 = list(map(int, Mat22)) 
Matrix_2_row_3 = input("Enter values for matrix 2 row 3 separated by commas: ") 
Mat23 = Matrix_2_row_3.split(",")
Mat23 = list(map(int, Mat23)) 
Sum = (str(Mat11[0] + Mat21[0])) + " "*2 + (str(Mat11[1] + Mat21[1])) +" "*2 + (str(Mat11[2] + Mat21[2])) + "\n" + (str(Mat12[0] + Mat22[0])) + " "*2 + 	(str(Mat12[1] + Mat22[1])) + " "*2 + 	(str(Mat12[2] +Mat22[2])) + "\n" + 	(str(Mat13[0] + Mat23[0])) + " "*2 + 	(str(Mat13[1] + Mat23[1])) + " "*2 + (str(Mat13[2] + Mat23[2]))
Subs = (str(Mat11[0] - Mat21[0])) + " "*2 + (str(Mat11[1] - Mat21[1])) +" "*2 + (str(Mat11[2] - Mat21[2])) + "\n" + 	(str(Mat12[0] - Mat22[0])) + " "*2 + (str(Mat12[1] - Mat22[1])) + " "*2 + 	(str(Mat12[2] - Mat22[2])) + "\n" + 	(str(Mat13[0] - Mat23[0])) + " "*2 + 	(str(Mat13[1] - Mat23[1])) + " "*2 + (str(Mat13[2] - Mat23[2]))
Mut = (str((Mat11[0]*Mat21[0] + 		Mat11[1]*Mat22[0] + Mat11[2]*	Mat23[0]))) + " "*2 + (str((Mat11[0]*	Mat21[1] + Mat11[1]*Mat22[1] + 	Mat11[2]*Mat23[1]))) + " "*2 + 			(str((Mat11[0]*Mat21[2] + Mat11[1]*Mat22[2] + Mat11[2]*Mat23[2]))) + "\n" + (str((Mat12[0]*Mat21[0] + 		Mat12[1]*Mat22[0] + Mat12[2]*	Mat23[0]))) + " "*2 + (str((Mat12[0]*	Mat21[1] + Mat12[1]*Mat22[1] + 		Mat12[2]*Mat23[1]))) + " "*2 + 		(str((Mat12[0]*Mat21[2] + Mat12[1]*Mat22[2] + Mat12[2]*Mat23[2]))) + 	"\n" + (str((Mat13[0]*Mat21[0] + 		Mat13[1]*Mat22[0] + Mat13[2]*		Mat23[0]))) + " "*2 + (str((Mat13[0]*	Mat21[1] + Mat13[1]*Mat22[1] + 	Mat13[2]*Mat23[1]))) + " "*2 + 			(str((Mat13[0]*Mat21[2] + Mat13[1]*Mat22[2] + Mat13[2]*Mat23[2])))
if Op==1:
	print("The answer is:\n" + str(Sum)) 
if Op==2:
	print("The answer is:\n" + str(Subs)) 
if Op==3:
	print("The answer is:\n" + str(Mut)) 