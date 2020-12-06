# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

def choices (values: List[float])->List[bool]:   # takes all the values that are over 7
    Is_Selected=[];
    for i in values:
        if(i>7):
            Is_Selected.append(True);
        else:
            Is_Selected.append(False);
    return Is_Selected;

def choices2 (values: List[float])->List[bool]: # takes the second max value - not monotonic
    Is_Selected=[];
    max=0;
    max2=0;
    count=0;
    intdex_max2=0;
    for i in values:
        Is_Selected.append(False);
        if(i>max):
            max2=max;
            intdex_max2=count;
            max=i;
        if(i<max and i>max2):
            max2=i;
            intdex_max2 = count;
        count = count + 1;

    Is_Selected[intdex_max2]=True;
    return Is_Selected;

def choices3 (values: List[float])->List[bool]: # Algorithm Chamdany A
    Is_Selected = [];
    values.sort();
    values.reverse();
    #print (values);
    Mg=100;
    Mg_Array = [];
    for i in values:
        Mg_Array.append(20);
    sum=0;
    flag=True; #can insert to bag
    #print(Mg_Array);
    for i in Mg_Array:
        if(sum+i<=Mg and flag==True):
            sum+=i;
            Is_Selected.append(True);
        else:
            Is_Selected.append(False);
            flag=False;
    return Is_Selected;

def payments (values: List[float])->List[float]:

   values.sort();
   values.reverse();
   print(values);
   flag=False; #Represents whether someone was selected already
   payment=[];
   for i in values:  #Open payment array in the same size as values
       payment.append(0);

   Is_Chosen = choices3(values);
   print("is chosen", Is_Chosen);
   for i in reversed(range(len(values))):
        if (Is_Chosen[i] == False):
            if (flag == True):  # not monotonic- the last one-j was chosen and i>j didnt
                raise Exception("not monotonic");
            else:
                payment[i]= 0;  # Not selected

        if(Is_Chosen[i]==True):
            #print(i,"chosen");
            flag=True;   # The selections after that i should be selected as well
            if(i== len(values)):   #The last i
                payment[i]=values[i];
            else:
                if(Is_Chosen[i+1]): #Pays like the previous participant-monotonic
                    payment[i]=payment[i+1];
                else:  #The previous participant was not selected and therefore pays its value
                    payment[i] = values[i+1];
   return payment;




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    List = [10,4,6,9,8,7,5];
    pay = payments(List);
    print("Payment of each one is=",pay);

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
