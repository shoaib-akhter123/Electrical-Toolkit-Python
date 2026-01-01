print("------------Program Name: Ohm's Law Calculator--------------------------------\n"
"------------Description: This program helps calculate electrical values------\n"
"-----------Instruction: Please choose one option to continue-----------------\n".upper())
again="YES"
while (again=="YES"):
     finding_value=int(input("choose 1 if finding voltage\n"
     "choose 2 if finding current\n"
     "choose 3 if finding ressistance\n"
     "choose 4 if finding power\n"
     "choose 5 if finding equavalient of series resistors\n"
     "choose 6 if finding equavalient of parallel resistors\n"
     "choose 7 if finding voltage across each resistor by vdr\n"
     "choose 8 if finding current across each resistor by cdr\n".upper()))
     print (" ------Enter Only Numeric Value------")
     if (finding_value == 1):
                r=float(input(" Enter value of resistance\n"))
                i=float(input(" Enter value of current\n"))
                voltage = i *r 
                print("The required voltage is:",voltage,"Volts")
     elif(finding_value == 2):
                r=float(input(" Enter value of resistance\n"))
                v=float(input(" Ente value of voltage\n"))   
                if (r==0):
                     print ("current is infinite and this is case of short circuit ")
                else:    
                     current = v/r
                     print("The required current is:",current ,"Amp")
     elif (finding_value == 3):
                i=float(input(" Enter value of current\n"))  
                v=float(input(" Ente value of voltage\n"))
                if (i==0):
                      print ("resistance  is infinite  ")
                else: 
                    resistance = v/i
                    print("The required resistance is:",resistance,"ohms")
     elif(finding_value == 4): 
          formula_choice=int(input("choose 1 if you have voltage and current\n"
          "choose 2 if you have voltage and resisttance\n"
          "choose 3 if you have cuurent and resistance\n ".upper())) 
          print (" ------Enter Only Numeric Value------")
          if (formula_choice==1):
                    i=float(input(" Enter value of current\n")) 
                    v=float(input(" Ente value of voltage\n")) 
                    power=i*v
                    print("power is" ,power, "watt")
          elif(formula_choice==2):
                          v=float(input(" Ente value of voltage\n")) 
                          r=float(input(" Enter value of resistance\n"))
                          if(r!=0):
                               power=(v**2)/r
                               print("power is" ,power, "watt") 
                          else:
                               print("power is infinite".upper())
          elif(formula_choice==3):
                     i=float(input(" Enter value of current\n"))
                     r=float(input(" Enter value of resistance\n"))
                     power=(i**2)*(r )
                     print("power is" ,power, "watt") 
     elif(finding_value==5):
          i=0
          total=0
          n_o_r=int(input("how many resistors ?"))
          if(n_o_r>1):
                while(i<n_o_r):
                    resistance=float(input("entre value of resistors \n".upper()))
                    total=total+resistance 
                    i=i+1
                print("SO EQUAVALIENT RESISTANCE OF RESISTORS IN SERIES =",total," ohm")
          else:
               print("resistors must be greather than one")
     elif(finding_value==6):
          i=0
          total=0
          n_o_r=int(input("how many resistors ?"))
          if(n_o_r>1):
                while(i<n_o_r):
                    resistance=float(input("entre value of resistors \n".upper()))
                    reci_resistance=(1)/(resistance)
                    total=total+reci_resistance
                    i=i+1
                print("SO EQUAVALIENT RESISTANCE OF RESISTORS IN PRALLEL =",total," ohm") 
          else:
               print("resistors must be greather than one")  
     elif(finding_value==7):  
          resis= float(input(" Enter value of resistance\n"))
          sum_resistors= float(input(" Enter value of equavalient resistance of resistors that are in series\n"))
          total_voltage= float(input(" Ente value of  total voltage\n"))
          v_a_r=((resis) /  (sum_resistors))*total_voltage
          print("SO THE VOLTAGE ACROSS GIVEN RESISTORS = " ,v_a_r ," Volts")
     elif(finding_value==8):  
          resis= float(input(" Enter value of resistance that are parallel to the resistor for which current required\n"))
          sum_resistors= float(input(" Enter value of equavalient resistance of resistors that are in series\n"))
          total_current= float(input(" Ente value of  total current\n"))
          c_a_r=((resis) /  (sum_resistors))*total_current
          print("SO THE VOLTAGE ACROSS GIVEN RESISTORS = " ,c_a_r ," Amp")
     else:
               print("invalid input") 
     again=input("do you want to calculate again(yes/no)".upper()).upper()
if(again=="NO"):
      print("thanks you for using this electrical calculator ".upper())






