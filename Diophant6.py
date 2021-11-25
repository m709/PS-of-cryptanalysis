# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#ГЕНЕТИЧЕСКИЙ АЛГОРИТМ, АДАПТИРОВАННЫЙ ДЛЯ РЕШЕНИЯ СИСТЕМ ДИОФАНТОВЫХ УРАВНЕНИЙ
#алгоритм написан!!!
#29.08.2021 я окончательно доработал эвристику №1 (с остатками от деления) и подключил её к основной программе!
#18.11.2021 поиск с запретами реализован!!!
import tkinter as tk
import random
import time
def st_mod(x,y,z): #функция, вычисляющая значение выражения (x^y) mod z #верно!
    if x==0:
        return 0
    else:
        u=x%z
        for i in range(1,y):
            u=(u*x)%z
        return u
#print(st_mod(3,3,19))
def vychets(modul,stepen): #эта функция составляет список всех вычетов степени stepen по модулю modul #верно!
    ost=set()
    for i in range(modul):
        u=st_mod(i,stepen,modul)
        ost.add(u)
    vych=[]
    for i in ost:
        vych.append(i)
    return vych
def gen_nabory(nvar,modul): #функция, которая генерирует список списков, в которых представлены все варианты остатков от деления на modul для nvar переменных
    vsego=modul**nvar
    res=[]
    for i in range(vsego):
        och=[]
        x=i; k=0
        while x>0:
            v=x%modul
            x=int(x/modul)
            och=[v]+och; k+=1
        while k<nvar:
            och=[0]+och; k+=1
        res.append(och)
    return res
#print(vychets(9,10))
"""nach=time.time()
list1=gen_nabory(5,9)
kon=time.time()
dlit=kon-nach
print(dlit)"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def c(x,y): #канторовская нумерация пар натуральных чисел
    return int(((x+y)*(x+y)+3*x+y)/2)
def pi(n,kor): #канторовская нумерация n-элементных кортежей натуральных чисел
    if(n==len(kor)):
        if(n>2):
            kor1=[];
            kor1.append(c(kor[0],kor[1]))
            for i in range(2,n):
                kor1.append(kor[i])
            return pi(n-1,kor1)
        else:
            return c(kor[0],kor[1])
    else:
        return None
def to_set(list):
    mn=[];
    for i in range(len(list)):
        j=0; flag=1;
        while((j<len(mn))and(flag==1)):
            if(mn[j]==list[i]):
                flag=0
            else:
                j=j+1
        if(flag==1):
            mn.append(list[i])
    return mn
#print(pi(4,[-2,0,-2,0]))
#print(to_set([[1,2],[1,2,2],[1,2,2,3],[1,2,2,9]]))
I=[]
N=[]
#err=0
def er(err): #процедура, генерирующая ошибку
    err=1
def abs(x):
    if(x<0):
        return (-1*x)
    else:
        return x
for i in range(100):
    I.append(""); N.append("")
R=["(",")"]
O=["+","-","*","/","^","="]
def p1(s):
    f=0; i=0; j=0;
    while((i<100)and(f==0)):
        if(I[i]==s):
            f=1; j=i;
        else:
            i=i+1
    if(f==0):
        i=0;
        while((i<100)and(I[i]!="")):
            i=i+1
        I[i]=s; return "I"+str(i)+" ";
    else:
        return "I"+str(j)+" "
def p3(s):
    f=0; i=0; j=0;
    while((i<100)and(f==0)):
        if(N[i]==s):
            f=1; j=i;
        else:
            i=i+1
    if(f==0):
        i=0;
        while((i<100)and(N[i]!="")):
            i=i+1
        N[i]=s; return "N"+str(i)+" ";
    else:
        return "N"+str(j)+" "
def p4(s):
    if(s=="("):
        return "R0 "
    if(s==")"):
        return "R1 "
def p6(s):
    if(s=="+"):
        return "O0 "
    if(s=="-"):
        return "O1 "
    if(s=="*"):
        return "O2 "
    if(s=="/"):
        return "O3 "
    if(s=="^"):
        return "O4 "
    if(s=="="):
        return "O5 "
def lex_an(s):
    res=""; err=0;
    i=0; buf="";
    if(s==""):
        err=1
    while((i<len(s))and(err==0)):
        if((i<len(s))and((s[i]>='a')and(s[i]<='z')or(s[i]>='A')and(s[i]<='Z')or(s[i]=='_') or (s[i]>='а') and (s[i]<='я') or (s[i]>='А')and (s[i]<='Я')or(s[i]=='ё')or (s[i]=='Ё'))):
            while((i<len(s))and((s[i]>='a')and(s[i]<='z')or(s[i]>='A')and(s[i]<='Z')or(s[i]=='_') or (s[i]>='а') and (s[i]<='я') or (s[i]>='А')and (s[i]<='Я')or(s[i]=='ё')or (s[i]=='Ё'))):
                buf=buf+s[i]; i=i+1;
            if((i<len(s))and(s[i]>='0')and(s[i]<='9')):
                while((i<len(s))and((s[i]>='a')and(s[i]<='z')or(s[i]>='A')and(s[i]<='Z')or(s[i]>='0')and(s[i]<='9')or(s[i]=='_') or (s[i]>='а') and (s[i]<='я') or (s[i]>='А')and (s[i]<='Я')or(s[i]=='ё')or (s[i]=='Ё'))):
                    buf=buf+s[i]; i=i+1;
                c=""
                if(i<len(s)):
                    c=""+s[i]; f=0;
                    if((c=="(")or(c==")")):
                        f=1
                    if((c=="+")or(c=="-")or(c=="*")or(c=="/")or(c=="^")or(c=="=")):
                        f=1
                    if(f==1):
                        res=res+p1(buf); buf="";
                    else:
                        err=1
                else:
                    res=res+p1(buf); buf="";
            else:
                c=""
                if(i<len(s)):
                    c=""+s[i]; f=0;
                    if((c=="(")or(c==")")):
                        f=1
                    if((c=="+")or(c=="-")or(c=="*")or(c=="/")or(c=="^")or(c=="=")):
                        f=1
                    if(f==1):
                        res=res+p1(buf); buf="";
                    else:
                        err=1
                else:
                    res=res+p1(buf); buf="";
        else:
            if((i<len(s))and(s[i]>='0')and(s[i]<='9')):
                while((i<len(s))and(s[i]>='0')and(s[i]<='9')):
                    buf=buf+s[i]; i=i+1;
                c=""
                if(i<len(s)):
                    c=""+s[i]; f=0;
                    if((c=="(")or(c==")")):
                        f=1
                    if((c=="+")or(c=="-")or(c=="*")or(c=="/")or(c=="^")or(c=="=")):
                        f=1
                    if(f==1):
                        res=res+p3(buf); buf="";
                    else:
                        err=1
                else:
                    res=res+p3(buf); buf="";
            else:
                if((i<len(s))and((s[i]=='(')or(s[i]==')'))):
                    buf=buf+s[i];
                    res=res+p4(buf);
                    buf=""
                    i=i+1
                else:
                    if((i<len(s))and((s[i]=='+')or(s[i]=='-')or(s[i]=='*')or(s[i]=='/')or(s[i]=='^')or(s[i]=='='))):
                        buf=buf+s[i];
                        res=res+p6(buf);
                        buf=""
                        i=i+1
                    else:
                        #i=i+1
                        err=1
    if(err==1):
        res="В уравнении есть не менее одной лексической ошибки."
    return res
def pow(x,y):
    if(y>=0):
        p=1
        for l in range(y):
            p=p*x;
        return p
    else:
        return None
def func(opz,param):
    stack=[];
    for i in range(100):
        stack.append(None);
    i=0; error=0;
    while((i<len(opz))and(error==0)):
        if(opz[i][0]=='I'):
            no=int(opz[i][1]);
            sch=0;
            while((sch<100)and(stack[sch]!=None)):
                sch=sch+1;
            stack[sch]=param[no];
            i=i+1
        else:
            if(opz[i][0]=='N'):
                no=int(opz[i][1]); sch=0;
                while((sch<100)and(stack[sch]!=None)):
                    sch=sch+1;
                stack[sch]=int(N[no]);
                i=i+1
            else:
                if(opz[i]=="O0"):
                    sch=0;
                    while((sch<100)and(stack[sch]!=None)):
                        sch=sch+1
                    if(sch-2>=0):
                        q=stack[sch-2]+stack[sch-1]; stack[sch-1]=None; stack[sch-2]=q; i=i+1
                    else:
                        #if(sch-1>=0):
                         #   q=0+stack[sch-1]; stack[sch-1]=q; i=i+1
                        #else:
                            error=1
                else:
                    if(opz[i]=="O1"):
                        sch = 0;
                        while((sch<100)and(stack[sch]!=None)):
                            sch=sch+1
                        if(sch-2>=0):
                            q=stack[sch-2]-stack[sch-1]; stack[sch-1]=None; stack[sch-2]=q;
                            i=i+1
                        else:
                            #if(sch-1>=0):
                              #  q=0-stack[sch-1]; stack[sch-1]=q;
                             #   i=i+1
                            #else:
                                error=1
                    else:
                        if(opz[i]=="O2"):
                            sch = 0;
                            while((sch<100)and(stack[sch]!=None)):
                                sch=sch+1
                            if(sch-2>=0):
                                q=stack[sch-2]*stack[sch-1]; stack[sch-1]=None; stack[sch-2]=q;
                                i=i+1
                            else:
                                error=1
                        else:
                            if(opz[i]=="O3"):
                                sch=0;
                                while((sch<100)and(stack[sch]!=None)):
                                    sch=sch+1
                                if(sch-2>=0):
                                    if(stack[sch-1]!=0):
                                        q=stack[sch-2]/stack[sch-1]; stack[sch-1]=None; stack[sch-2]=q;
                                        i=i+1
                                    else:
                                        error=1
                                else:
                                    error=1
                            else:
                                if(opz[i]=="O4"):
                                    sch=0;
                                    while((sch<100)and(stack[sch]!=None)):
                                        sch=sch+1
                                    if(sch-2>=0):
                                        q=pow(stack[sch-2],stack[sch-1]); stack[sch-1]=None; stack[sch-2]=q;
                                        i=i+1;
                                    else:
                                        error=1
                                else:
                                    error=1
    sch=0
    while((sch<100)and(stack[sch]!=None)):
        sch=sch+1
    if(error==0):
        return stack[sch-1]
    else:
        return None
    #print(stack)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print(int(None)+1)
    window = tk.Tk()
    te="Введите диофантово уравнение\n или систему диофантовых уравнений\n (уравнения в системе записываются через запятую):"
    #textView=tk.Text() это раньше было
    textView = tk.Label(text=te,fg="black",bg="gray",width=50,height=5)
    #textView.insert("1.0",te)
    textView.pack()
    editText = tk.Entry(width=100)
    editText.pack()
    """tv1=tk.Text()
    tv1.insert("1.0","Число хромосом в первом поколении:")"""
    tv1=tk.Label(text="Число хромосом в первом поколении:",fg="black",bg="gray",width=30,height=3)
    tv1.pack()
    et1=tk.Entry(width=10)
    et1.pack()
    """tv2=tk.Text()
    tv2.insert("1.0","Максимальное число поколений:")"""
    tv2=tk.Label(text="Максимальное число поколений:", fg="black", bg="gray", width=30, height=3)
    tv2.pack()
    et2=tk.Entry(width=10)
    et2.pack()
    tv3=tk.Label(text="Ограничения на значения неизвестных:", fg="black", bg="gray", width=40, height=3)
    tv3.pack()
    et3=tk.Entry(width=100)
    et3.pack()
    count=0; summa=0; sred=0; maxti=0; count1=0;

    def ONCLICK():
        global count; global summa; global sred; global maxti; global count1;
        s = editText.get()
        ur=s.split(',') #получаем список всех записанных уравнений
        #print("&&&&&&&&&&&&&&&&&&&&&&&&&&"); print(ur); print("&&&&&&&&&&&&&&&&&&&&&&&&&&");
        s1=et1.get(); s2=et2.get(); s3=et3.get()
        textView2.delete("1.0", tk.END)
        for i in range(100):
            I[i] = "";
            N[i] = "";
        # textView2.insert("1.0",s)
        res_=[]
        for w in ur:
            res_.append(lex_an(w))
        flag=1; w=0
        while w<len(res_) and flag==1:
            if res_[w]=="В уравнении есть не менее одной лексической ошибки.":
                flag=0
            else:
                w+=1
        # textView2.insert("1.0",res)
        if flag==1:
            #textView2.insert("1.0", "В записанном уравнении или системе уравнений нет лексических ошибок.")
            nur=len(res_) #число уравнений в системе
            le=[]; #список списков лексем всех уравнений
            for i in range(nur):
                le_=[]; st=""
                for j in range(len(res_[i])):
                    if res_[i][j]==' ':
                        le_.append(st); st=""
                    else:
                        st+=res_[i][j]
                le.append(le_)
            #print(le)
            nra=[] #список, в котором содержится число знаков равенства в каждом уравнении системы
            for i in le:
                nra.append(i.count("O5"))
            #print(nra)
            flag1=1; w=0;
            while w<len(nra) and flag1==1: #проверим, во всех ли уравнениях системы содержится ровно один знак равенства
                if nra[w]!=1:
                    flag1=0
                else:
                    w+=1
            #print(flag1)
            if flag1==1:
                #textView2.insert("1.0", "Во всех записанных уравнениях есть точно один знак равенства.")
                w=0; flag2=1; in_=[]
                while w<len(le) and flag2==1:
                    ind=le[w].index("O5");
                    if ind==len(le[w])-1:
                        flag2=0
                    else:
                        w+=1
                #print(flag2)
                if flag2==1:
                    #textView2.insert("1.0", "Правая часть всех записанных уравнений присутствует.")
                    #теперь нужно проверить наличие левой части
                    w=0; flag3=1;
                    while w<len(le) and flag3==1:
                        ind=le[w].index("O5");
                        if ind==0:
                            flag3=0
                        else:
                            w+=1
                    #print(flag3)
                    if flag3==1:
                        #textView2.insert("1.0", "Левая часть всех записанных уравнений присутствует.")
                        le1=[]
                        for i in range(len(le)):
                            le1.append([])
                        #правую часть каждого уравнения переносим влево и записываем результат в список le1
                        for i in range(len(le)):
                            ind=le[i].index("O5")
                            for j in range(ind):
                                le1[i].append(le[i][j])
                            le1[i].append("O1"); le1[i].append("R0")
                            for j in range(ind+1,len(le[i])):
                                le1[i].append(le[i][j])
                            le1[i].append("R1")
                        #print(le1)
                        #составить на основе списка le1 ОПЗ каждого уравнения и применить эвристику к каждому уравнению!!!
                        POLIZ=[] #список из ОПЗ каждого уравнения системы
                        ne=len(le1)
                        for i in range(ne):
                            POLIZ.append([]) #ОПЗ каждого уравнения будет являться списком
                        prior = []  # список операций, упорядоченных по приоритету
                        for i in range(5):
                            prior.append([])
                        for i in range(5):
                            for j in range(2):
                                prior[i].append("")
                        prior[0][0] = "R0";
                        prior[1][0] = "R1";
                        prior[2][0] = "O0";
                        prior[2][1] = "O1";
                        prior[3][0] = "O2";
                        prior[3][1] = "O3";
                        prior[4][0] = "O4";
                        for i in range(ne):
                            stack = [];  # стэк операций
                            for j in range(100):
                                stack.append("")
                            щ=len(le1[i])
                            for j in range(щ):
                                if le1[i][j] == "O0" or le1[i][j] == "O1" or le1[i][j] == "O2" or le1[i][j] == "O3" or le1[i][j] == "O4":
                                    pust = 1; z = 0;
                                    while z < 100 and pust == 1:  # проверяем, не лежат ли в стэке какие-нибудь операции
                                        if stack[z] != "":
                                            pust = 0
                                        else:
                                            z = z + 1
                                    if pust == 1:  # Если не лежат,
                                        stack[0] = le1[i][j]  # то добавляем текущую лексему в стэк.
                                    else:  # а если лежат, то...
                                        w = 0; f2 = 0; verh = -1;
                                        while w < 100 and f2 == 0:
                                            if stack[w] == "":
                                                f2 = 1; verh = w;
                                            else:
                                                w = w + 1;
                                        verh = verh - 1;
                                        x = 0;
                                        flag = 0;
                                        pr_v = -1;
                                        # найдём приоритет верхушки стэка:
                                        while x < 5 and flag == 0:
                                            if prior[x][0] == stack[verh] or prior[x][1] == stack[verh]:
                                                flag = 1;
                                                pr_v = x;
                                            else:
                                                x = x + 1;
                                        # найдём приоритет текущей операции:
                                        x = 0; flag = 0; pr_o = -1;
                                        while x < 5 and flag == 0:
                                            if prior[x][0] == le1[i][j] or prior[x][1] == le1[i][j]:
                                                flag = 1;
                                                pr_o = x;
                                            else:
                                                x = x + 1;
                                        if pr_v < pr_o:
                                            if verh + 1 < 100:
                                                stack[verh + 1] = le1[i][j]
                                        else:
                                            POLIZ[i].append(stack[verh]);
                                            stack[verh] = "";
                                            z1 = verh - 1;
                                            flag1 = 1;
                                            if z1 == -1:
                                                stack[0] = le1[i][j]
                                            while z1 >= 0 and flag1 == 1:
                                                if z1 == -1:
                                                    stack[0] = le1[i][j]
                                                else:
                                                    x = 0; flag = 0; pr_v = -1;
                                                    # найдём приоритет верхушки стэка:
                                                    while x < 5 and flag == 0:
                                                        if prior[x][0] == stack[z1] or prior[x][1] == stack[z1]:
                                                            flag = 1; pr_v = x;
                                                        else:
                                                            x = x + 1;
                                                    if pr_v < pr_o:
                                                        flag1 = 0;
                                                        if z1 + 1 < 100:
                                                            stack[z1 + 1] = le1[i][j]
                                                    else:
                                                        POLIZ[i].append(stack[z1]);
                                                        stack[z1] = "";
                                                        z1 = z1 - 1;
                                            if z1 + 1 < 100:
                                                stack[z1 + 1] = le1[i][j];
                                else:
                                    if le1[i][j] == "R0":
                                        z = 0
                                        while z < 100 and stack[z] != "":
                                            z = z + 1;
                                        if z < 100:
                                            stack[z] = le1[i][j]
                                    else:
                                        if le1[i][j] == "R1":
                                            z = 0
                                            while z < 100 and stack[z] != "":
                                                z = z + 1
                                            z = z - 1
                                            while z >= 0 and stack[z] != "R0":
                                                POLIZ[i].append(stack[z]);
                                                stack[z] = "";
                                                z = z - 1;
                                            if z >= 0:
                                                if stack[z] == "R0":
                                                    stack[z] = ""
                                        else:
                                            POLIZ[i].append(le1[i][j])
                            v=0; fl1 = 0;
                            while v < 100 and fl1 == 0:
                                if stack[v] == "":
                                    fl1 = 1
                                else:
                                    v = v + 1
                            v = v - 1;
                            while v >= 0:
                                POLIZ[i].append(stack[v]);
                                v = v - 1;
                            # print(opz) #проверена правильность перевода в ОПЗ каждого уравнения. Перевод выполняется верно.
                        #теперь составляем сумму квадратов левых частей уравнений и результат записываем в список le2
                        le2=[]
                        for i in range(len(le)):
                            le2.append("R0")
                            for j in range(len(le1[i])):
                                le2.append(le1[i][j])
                            le2.append("R1")
                            le2.append("O4")
                            le2.append(p3("2"))
                            if i<len(le)-1:
                                le2.append("O0")
                        #print(le2) #проверено
                        #считаем число переменных в уравнении
                        x=0;
                        while x<len(I) and I[x]!="":
                            x=x+1;
                        kper=x;
                        if kper>1 and s1.isnumeric() and s2.isnumeric():
                            n1=int(s1); max_gen=int(s2)
                            if n1>0 and max_gen>0:
                                if kper<=6: #если суммарное число неизвестных в уравнении или системе не больше шести, то запускаем эвристику №1 (с остатками)
                                    _1 = time.time()
                                    мо = 9
                                    para = gen_nabory(kper, мо)
                                    т_ = 0; ф_ = 1; ы_ = len(para); ф__ = 1
                                    while т_ < ne and ф_ == 1 and ф__ == 1:
                                        osta = set()
                                        for я_ in range(ы_):
                                            if func(POLIZ[т_], para[я_]) != None:
                                                ostatok = func(POLIZ[т_], para[я_]) % мо
                                                osta.add(ostatok)
                                            else:
                                                osta.add(None)
                                        if not (None in osta):
                                            if not (0 in osta):
                                                ф_ = 0
                                            else:
                                                т_ += 1
                                        else:
                                            ф__ = 0
                                    _2 = time.time()
                                    _3 = _2 - _1
                                    """print("////////////////////////////////////////")
                                    print(ф_)
                                    print(_3)"""
                                    #print("////////////////////////////////////////")
                                    if ф__ == 1:
                                        if ф_ == 0:  # первая эвристика установила, что решений нет.
                                            textView2.insert("1.0", "Введённое уравнение или система не имеет решений.")
                                            textView2.insert("2.0", "\n")
                                            textView2.insert("3.0", "Время работы программы: " + str(_3) + " секунды.")
                                            textView2.insert("4.0", "\n");
                                            count += 1; summa += _3; sred = summa / count;
                                            if _3 > maxti:
                                                maxti = _3;
                                            textView2.insert("5.0","Среднее время выполнения: " + str(sred) + " секунды.")
                                            textView2.insert("6.0", "\n")
                                            textView2.insert("7.0", "Программу запускали " + str(count) + " раз.")
                                            textView2.insert("8.0", "\n")
                                            textView2.insert("9.0", "Максимальное время выполнения программы: " + str(maxti) + " секунды.")
                                            textView2.insert("10.0","Хотя бы 1 решение нашлось в " + str(count1) + " случаях.")
                                        else:
                                            #print("Введённое уравнение или система, вероятно, имеет решения.")
                                            opz = []  # ОПЗ суммы квадратов уравнений
                                            prior = []  # список операций, упорядоченных по приоритету
                                            for i in range(5):
                                                prior.append([])
                                            for i in range(5):
                                                for j in range(2):
                                                    prior[i].append("")
                                            prior[0][0] = "R0";
                                            prior[1][0] = "R1";
                                            prior[2][0] = "O0"; prior[2][1] = "O1";
                                            prior[3][0] = "O2"; prior[3][1] = "O3";
                                            prior[4][0] = "O4";
                                            stack = [];  # стэк операций
                                            for i in range(100):
                                                stack.append("")
                                            щ = len(le2)
                                            for i in range(щ):
                                                if le2[i] == "O0" or le2[i] == "O1" or le2[i] == "O2" or le2[i] == "O3" or le2[i] == "O4":
                                                    pust = 1; z = 0;
                                                    while z < 100 and pust == 1:  # проверяем, не лежат ли в стэке какие-нибудь операции
                                                        if stack[z] != "":
                                                            pust = 0
                                                        else:
                                                            z = z + 1
                                                    if pust == 1:  # Если не лежат,
                                                        stack[0] = le2[i]  # то добавляем текущую лексему в стэк.
                                                    else:  # а если лежат, то...
                                                        w = 0; f2 = 0; verh = -1;
                                                        while w < 100 and f2 == 0:
                                                            if stack[w] == "":
                                                                f2 = 1; verh = w;
                                                            else:
                                                                w = w + 1;
                                                        verh = verh - 1;
                                                        x = 0; flag = 0; pr_v = -1;
                                                        # найдём приоритет верхушки стэка:
                                                        while x < 5 and flag == 0:
                                                            if prior[x][0] == stack[verh] or prior[x][1] == stack[verh]:
                                                                flag = 1; pr_v = x;
                                                            else:
                                                                x = x + 1;
                                                        # найдём приоритет текущей операции:
                                                        x = 0; flag = 0; pr_o = -1;
                                                        while x < 5 and flag == 0:
                                                            if prior[x][0] == le2[i] or prior[x][1] == le2[i]:
                                                                flag = 1; pr_o = x;
                                                            else:
                                                                x = x + 1;
                                                        if pr_v < pr_o:
                                                            if verh + 1 < 100:
                                                                stack[verh + 1] = le2[i]
                                                        else:
                                                            opz.append(stack[verh]); stack[verh] = "";
                                                            z1 = verh - 1; flag1 = 1;
                                                            if z1 == -1:
                                                                stack[0] = le2[i]
                                                            while z1 >= 0 and flag1 == 1:
                                                                if z1 == -1:
                                                                    stack[0] = le2[i]
                                                                else:
                                                                    x = 0; flag = 0; pr_v = -1;
                                                                    # найдём приоритет верхушки стэка:
                                                                    while x < 5 and flag == 0:
                                                                        if prior[x][0] == stack[z1] or prior[x][1] == stack[z1]:
                                                                            flag = 1; pr_v = x;
                                                                        else:
                                                                            x = x + 1;
                                                                    if pr_v < pr_o:
                                                                        flag1 = 0;
                                                                        if z1 + 1 < 100:
                                                                            stack[z1 + 1] = le2[i]
                                                                    else:
                                                                        opz.append(stack[z1]); stack[z1] = ""; z1 = z1 - 1;
                                                            if z1 + 1 < 100:
                                                                stack[z1 + 1] = le2[i];
                                                else:
                                                    if le2[i] == "R0":
                                                        z = 0
                                                        while z < 100 and stack[z] != "":
                                                            z = z + 1;
                                                        if z < 100:
                                                            stack[z] = le2[i]
                                                    else:
                                                        if le2[i] == "R1":
                                                            z = 0
                                                            while z < 100 and stack[z] != "":
                                                                z = z + 1
                                                            z = z - 1
                                                            while z >= 0 and stack[z] != "R0":
                                                                opz.append(stack[z]); stack[z] = ""; z = z - 1;
                                                            if z >= 0:
                                                                if stack[z] == "R0":
                                                                    stack[z] = ""
                                                        else:
                                                            opz.append(le2[i])
                                            v = 0; fl1 = 0;
                                            while v < 100 and fl1 == 0:
                                                if stack[v] == "":
                                                    fl1 = 1
                                                else:
                                                    v = v + 1
                                            v = v - 1;
                                            while v >= 0:
                                                opz.append(stack[v]); v = v - 1;
                                            # print(opz) #проверено
                                            """фа = open("resheno.txt", 'r')
                                            resh_ur = фа.readlines()
                                            фа.close()
                                            mn_ur = set(resh_ur)
                                            mn_ur.add(str(opz) + "\n")
                                            resh_ur = []
                                            for ъ in mn_ur:
                                                resh_ur.append(ъ)
                                            фа = open("resheno.txt", 'w'); n_resh_ur=len(resh_ur)
                                            for ъ in range(n_resh_ur):
                                                фа.write(resh_ur[ъ])  # записываем ОПЗ решённых уравнений и систем в файл, чтобы потом их оттуда доставать при необходимости
                                            фа.close()"""
                                            # соберём массив числовых констант в итоговом уравнении, чтобы знать, какого порядка числа в нём есть
                                            chisla = []; o = 0;
                                            while o < 100 and N[o] != "":
                                                chisla.append(int(N[o])); o += 1
                                            if len(chisla) == 0:  # если числа не используются, предполагается, что используются коэффициенты 1 или -1 в зависимости от операции. Например, в уравнении x+y=z<=>x+y-z=0
                                                # Такой вариант гарантирует, что список чисел будет точно непустым, так как в левой части уравнения всегда будет хотя бы одна операция вычитания в связи с переносом правой части исходного уравнения влево
                                                le3 = len(opz)
                                                for i_ in range(le3):
                                                    if opz[i_] == "O0":
                                                        chisla.append(1)
                                                    else:
                                                        if opz[i_] == "O1":
                                                            chisla.append(-1)
                                            # print(chisla) #проверено
                                            chisla.sort();
                                            nn = len(chisla);
                                            min_n = chisla[0]; max_n = chisla[nn - 1]; sr = sum(chisla) / nn
                                            if nn % 2 == 0:
                                                med = (chisla[int(nn / 2) - 1] + chisla[int(nn / 2)]) / 2
                                            else:
                                                med = chisla[int((nn + 1) / 2) - 1]
                                            # print(chisla, nn, min_n, max_n, sr, med, end=" #\n") #проверено
                                            ogranich=0 #по умолчанию нет ограничений на корни уравнения (системы)
                                            err_ogranich=1 #маркер ошибки в записи ограничений
                                            text_err_ogranich="" #текст сообщения об ошибке в записи ограничений
                                            if len(s3)>0:
                                                ogranich=1 #уже какие-то ограничения есть, пусть даже и неверно записанные
                                                usl=s3.split(',') #список ограничений
                                                #print(usl)
                                                n_usl=len(usl) #число ограничений
                                                for д in range(n_usl):
                                                    л=""; ж=len(usl[д])
                                                    for ъ in range(ж):
                                                        if usl[д][ъ]!=' ':
                                                            л+=usl[д][ъ]
                                                    usl[д]=л
                                                #print(usl)
                                                ogr=[]
                                                for д in range(n_usl):
                                                    ogr.append([])
                                                for д in range(n_usl):
                                                    л=""; ж = len(usl[д]); ъ=0
                                                    while ъ<ж and usl[д][ъ]!='<' and usl[д][ъ]!='>' and usl[д][ъ]!='=':
                                                        л+=usl[д][ъ]; ъ+=1;
                                                    if ъ<ж:
                                                        if usl[д][ъ]=='<' or usl[д][ъ]=='>':
                                                            if ъ<ж-1 and usl[д][ъ+1]=='=':
                                                                ogr[д].append(usl[д][ъ]+usl[д][ъ+1])
                                                                ъ+=2
                                                            else:
                                                                ogr[д].append(usl[д][ъ])
                                                                ъ += 1
                                                        else:
                                                            if usl[д][ъ] == '=':
                                                                ogr[д].append(usl[д][ъ])
                                                                ъ += 1
                                                        if len(л)>0:
                                                            й=0
                                                            while й<100 and I[й]!=л:
                                                                й+=1
                                                            if й<100:
                                                                ogr[д].append(й)
                                                                л1=""
                                                                while ъ<ж:
                                                                    л1+=usl[д][ъ]
                                                                    ъ+=1
                                                                фл=1; сч=0; лл1=len(л1)
                                                                while сч<лл1 and фл==1:
                                                                    if л1[сч]<'0' or л1[сч]>'9':
                                                                        фл = 0
                                                                    else:
                                                                        сч+=1
                                                                if фл==1 and лл1>0:
                                                                    ogr[д].append(int(л1))
                                                                else:
                                                                    text_err_ogranich = "По крайней мере в одном ограничении неправильно написано число."
                                                            else:
                                                                text_err_ogranich ="По крайней мере в одном ограничении есть переменная, которой нет ни в одном из записанных уравнений."
                                                        else:
                                                            text_err_ogranich = "По крайней мере в одном ограничении перед знаком равенства или неравенства ничего не написано."
                                                    else:
                                                        text_err_ogranich = "По крайней мере в одном ограничении нет знака неравенства или равенства."
                                                if text_err_ogranich=="":
                                                    err_ogranich=0
                                                    print(ogr)
                                                else:
                                                    print(text_err_ogranich)
                                            # Генетический алгоритм:
                                            start = time.time()  # засекаем время начала работы генетического алгоритма
                                            hrom1 = []  # список хромосом первого поколения
                                            # n1 = int(s1)
                                            for i in range(n1):
                                                hrom1.append([])
                                            for i in range(n1):
                                                for j in range(kper):
                                                    hrom1[i].append(random.randint(-10, 10))
                                            for i in range(n1):
                                                if func(opz, hrom1[i]) != 0:  # хромосома мутирует с вероятностью 1, но только если она не является решением уравнения
                                                    rg = random.randint(0,kper - 1)  # выбираем случайный мутирующий ген
                                                    hrom1[i][rg] = random.randint(-1000, 1000)
                                                    if func(opz, hrom1[i]) != 0:  # если после первой мутации хромосома не стала решением уравнения, то проводим вторую мутацию
                                                        rg2 = random.randint(0,kper - 1)  # выбираем второй мутирующий ген
                                                        if int(med) < int(sr):
                                                            hrom1[i][rg2] = random.randint(int(med), int(sr))
                                                        else:
                                                            hrom1[i][rg2] = random.randint(int(sr), int(med))
                                                        if func(opz, hrom1[i]) != 0:  # если и вторая мутация не помогла, то проводим третью мутацию
                                                            rg3 = random.randint(0, kper - 1)
                                                            hrom1[i][rg3] = random.randint(-5, 5)
                                            resh = []  # список найденных решений
                                            for i in range(n1):
                                                if func(opz, hrom1[i]) == 0:
                                                    resh.append(hrom1[i])
                                            re1 = to_set(resh)
                                            n2 = int(n1 * (n1 - 1) / 2)
                                            hrom2 = [];  # список хромосом второго поколения
                                            for i in range(n2):
                                                hrom2.append([])
                                            h = 0
                                            for i in range(n1):
                                                for j in range(i + 1, n1):
                                                    t = random.randint(0, kper - 2)
                                                    for j1 in range(t):
                                                        hrom2[h].append(hrom1[i][j1])
                                                    for j1 in range(t, kper):
                                                        hrom2[h].append(hrom1[j][j1])
                                                    h = h + 1
                                            # print(hrom2)
                                            for i in range(n2):
                                                if func(opz, hrom2[i]) != 0:
                                                    rg = random.randint(0,kper - 1)  # выбираем случайный мутирующий ген
                                                    hrom2[i][rg] = random.randint(-1000, 1000)
                                                    if func(opz, hrom2[i]) != 0:
                                                        rg2 = random.randint(0,kper - 1)  # выбираем второй мутирующий ген
                                                        if int(med) < int(sr):
                                                            hrom2[i][rg2] = random.randint(int(med), int(sr))
                                                        else:
                                                            hrom2[i][rg2] = random.randint(int(sr), int(med))
                                                        if func(opz, hrom2[i]) != 0:
                                                            rg3 = random.randint(0, kper - 1)
                                                            hrom2[i][rg3] = random.randint(-5, 5)
                                            for i in range(n2):
                                                if func(opz, hrom2[i]) == 0:
                                                    resh.append(hrom2[i])
                                            re2 = to_set(resh)
                                            ge = 2  # число уже сгенерированных поколений
                                            flag_ = 2
                                            if re1 == re2 and re1 != []:
                                                flag_ = 1
                                            else:
                                                flag_ = 0
                                            # max_gen = int(s2)
                                            while ge <= max_gen and flag_ == 0:
                                                re1 = re2; hrom_ = []; n_ = int(n1 * (n1 - 1) / 2);
                                                for i in range(n_):
                                                    hrom_.append([])
                                                h = 0
                                                for i in range(n1):
                                                    for j in range(i + 1, n1):
                                                        t = random.randint(0, kper - 2)
                                                        for j1 in range(t):
                                                            hrom_[h].append(hrom2[i][j1])
                                                        for j1 in range(t, kper):
                                                            hrom_[h].append(hrom2[j][j1])
                                                        h = h + 1
                                                # проведём мутацию в очередном поколении в ~mut доли случаев
                                                for i in range(n_):
                                                    if func(opz, hrom_[i]) != 0:
                                                        rg = random.randint(0,kper - 1)  # выбираем случайный мутирующий ген
                                                        hrom_[i][rg] = random.randint(-1000, 1000)
                                                        if func(opz, hrom_[i]) != 0:
                                                            rg2 = random.randint(0,kper - 1)  # выбираем второй мутирующий ген
                                                            if int(med) < int(sr):
                                                                hrom_[i][rg2] = random.randint(int(med), int(sr))
                                                            else:
                                                                hrom_[i][rg2] = random.randint(int(sr), int(med))
                                                            if func(opz, hrom_[i]) != 0:
                                                                rg3 = random.randint(0, kper - 1)
                                                                hrom_[i][rg3] = random.randint(-5, 5)
                                                for i in range(n_):
                                                    if func(opz, hrom_[i]) == 0:
                                                        resh.append(hrom_[i])
                                                re2 = to_set(resh)
                                                if re1 == re2 and re1 != []:
                                                    flag_ = 1
                                                else:
                                                    ge = ge + 1
                                                hrom2 = hrom_
                                            res_s = ""
                                            if ogranich==0 or err_ogranich==1:
                                                for i in range(len(re2)):
                                                    stro = "";
                                                    for j in range(kper):
                                                        stro = stro + I[j] + "=" + str(re2[i][j]) + "\n"
                                                    res_s = res_s + stro + "\n"
                                            else: #в этом случае есть ограничения, написанные без ошибок. Нужно обработать этот случай.
                                                for i in range(len(re2)):
                                                    flag_ogr=1; ц=0
                                                    while ц<n_usl and flag_ogr==1:
                                                        if ogr[ц][0]=='<':
                                                            if re2[i][ogr[ц][1]]>=ogr[ц][2]:
                                                                flag_ogr=0
                                                        if ogr[ц][0]=='>':
                                                            if re2[i][ogr[ц][1]]<=ogr[ц][2]:
                                                                flag_ogr=0
                                                        if ogr[ц][0]=='=':
                                                            if re2[i][ogr[ц][1]]!=ogr[ц][2]:
                                                                flag_ogr=0
                                                        if ogr[ц][0]=='<=':
                                                            if re2[i][ogr[ц][1]]>ogr[ц][2]:
                                                                flag_ogr=0
                                                        if ogr[ц][0]=='>=':
                                                            if re2[i][ogr[ц][1]]<ogr[ц][2]:
                                                                flag_ogr=0
                                                        if flag_ogr==1:
                                                            ц+=1
                                                    if flag_ogr==1:
                                                        stro = "";
                                                        for j in range(kper):
                                                            stro = stro + I[j] + "=" + str(re2[i][j]) + "\n"
                                                        res_s = res_s + stro + "\n"
                                            finish = time.time()  # засекаем время окончания работы генетического алгоритма
                                            ti = finish - start  # время выполнения генетического алгоритма
                                            if len(re2) > 0:
                                                count += 1; summa += ti; sred = summa / count; count1 += 1;
                                                if ti > maxti:
                                                    maxti = ti;
                                                if ogranich==1 and err_ogranich==0:
                                                    if res_s=="":
                                                        textView2.insert("1.0","Не нашлось решений, удовлетворяющих заданным ограничениям, но нашлись другие решения." + "\n" + "Время выполнения генетического алгоритма: " + str(ti) + " секунды.\nСреднее время выполнения: " + str(sred) + " секунды.\nПрограмму запускали " + str(count) + " раз.\nМаксимальное время выполнения: " + str(maxti) + " секунды. Хотя бы 1 решение нашлось в " + str(count1) + " случаях.")
                                                    else:
                                                        textView2.insert("1.0","Найденные решения, удовлетворяющие указанным ограничениям:\n" + res_s + "\n" + "Время выполнения генетического алгоритма: " + str(ti) + " секунды.\nСреднее время выполнения: " + str(sred) + " секунды.\nПрограмму запускали " + str(count) + " раз.\nМаксимальное время выполнения: " + str(maxti) + " секунды. Хотя бы 1 решение нашлось в " + str(count1) + " случаях.")
                                                else:
                                                    if ogranich==1 and err_ogranich==1:
                                                        textView2.insert("1.0",text_err_ogranich+"\n"+"Найденные решения:\n" + res_s + "\n" + "Время выполнения генетического алгоритма: " + str(ti) + " секунды.\nСреднее время выполнения: " + str(sred) + " секунды.\nПрограмму запускали " + str(count) + " раз.\nМаксимальное время выполнения: " + str(maxti) + " секунды. Хотя бы 1 решение нашлось в " + str(count1) + " случаях.")
                                                    else:
                                                        textView2.insert("1.0","Найденные решения:\n" + res_s + "\n" + "Время выполнения генетического алгоритма: " + str(ti) + " секунды.\nСреднее время выполнения: " + str(sred) + " секунды.\nПрограмму запускали " + str(count) + " раз.\nМаксимальное время выполнения: " + str(maxti) + " секунды. Хотя бы 1 решение нашлось в " + str(count1) + " случаях.")
                                                # textView2.insert("3.0","Время выполнения генетического алгоритма: "+str(ti)+" секунды.")
                                            else:
                                                if ogranich == 1 and err_ogranich == 0:
                                                    textView2.insert("1.0", "К сожалению, никаких решений не нашлось.")
                                                else:
                                                    if ogranich == 1 and err_ogranich == 1:
                                                        textView2.insert("1.0",text_err_ogranich+"\n"+"К сожалению, никаких решений не нашлось.")
                                                    else:
                                                        textView2.insert("1.0","К сожалению, решений не нашлось.")
                                                textView2.insert("2.0", "\n")
                                                textView2.insert("3.0","Время выполнения генетического алгоритма: " + str(ti) + " секунды.")
                                                textView2.insert("4.0", "\n");
                                                count += 1; summa += ti; sred = summa / count;
                                                if ti > maxti:
                                                    maxti = ti;
                                                textView2.insert("5.0","Среднее время выполнения: " + str(sred) + " секунды.")
                                                textView2.insert("6.0", "\n")
                                                textView2.insert("7.0", "Программу запускали " + str(count) + " раз.")
                                                textView2.insert("8.0", "\n")
                                                textView2.insert("9.0","Максимальное время выполнения программы: " + str(maxti) + " секунды.")
                                                textView2.insert("10.0", "Хотя бы 1 решение нашлось в " + str(count1) + " случаях.")
                                    else:
                                        textView2.insert("1.0","В уравнении или системе есть синтаксические ошибки или используется унарный минус, который не поддерживается программой.")
                                    #print("////////////////////////////////////////")
                                else: #если же суммарное число неизвестных в уравнении или системе больше шести, то запускаем генетический алгоритм без эвристики №1
                                    # всё верно, можно запускать генетический алгоритм
                                    # сначала переведём в ОПЗ сумму квадратов левых частей уравнений (le2)
                                    # textView2.insert("1.0", "Всё записано верно, можно запускать генетический алгоритм.")
                                    opz = []  # ОПЗ суммы квадратов уравнений
                                    prior = []  # список операций, упорядоченных по приоритету
                                    for i in range(5):
                                        prior.append([])
                                    for i in range(5):
                                        for j in range(2):
                                            prior[i].append("")
                                    prior[0][0] = "R0";
                                    prior[1][0] = "R1";
                                    prior[2][0] = "O0"; prior[2][1] = "O1";
                                    prior[3][0] = "O2"; prior[3][1] = "O3";
                                    prior[4][0] = "O4";
                                    stack = [];  # стэк операций
                                    for i in range(100):
                                        stack.append("")
                                    щ = len(le2)
                                    for i in range(щ):
                                        if le2[i] == "O0" or le2[i] == "O1" or le2[i] == "O2" or le2[i] == "O3" or le2[i] == "O4":
                                            pust = 1; z = 0;
                                            while z < 100 and pust == 1:  # проверяем, не лежат ли в стэке какие-нибудь операции
                                                if stack[z] != "":
                                                    pust = 0
                                                else:
                                                    z = z + 1
                                            if pust == 1:  # Если не лежат,
                                                stack[0] = le2[i]  # то добавляем текущую лексему в стэк.
                                            else:  # а если лежат, то...
                                                w = 0; f2 = 0; verh = -1;
                                                while w < 100 and f2 == 0:
                                                    if stack[w] == "":
                                                        f2 = 1; verh = w;
                                                    else:
                                                        w = w + 1;
                                                verh = verh - 1; x = 0; flag = 0; pr_v = -1;
                                                # найдём приоритет верхушки стэка:
                                                while x < 5 and flag == 0:
                                                    if prior[x][0] == stack[verh] or prior[x][1] == stack[verh]:
                                                        flag = 1; pr_v = x;
                                                    else:
                                                        x = x + 1;
                                                # найдём приоритет текущей операции:
                                                x = 0; flag = 0; pr_o = -1;
                                                while x < 5 and flag == 0:
                                                    if prior[x][0] == le2[i] or prior[x][1] == le2[i]:
                                                        flag = 1; pr_o = x;
                                                    else:
                                                        x = x + 1;
                                                if pr_v < pr_o:
                                                    if verh + 1 < 100:
                                                        stack[verh + 1] = le2[i]
                                                else:
                                                    opz.append(stack[verh]); stack[verh] = "";
                                                    z1 = verh - 1; flag1 = 1;
                                                    if z1 == -1:
                                                        stack[0] = le2[i]
                                                    while z1 >= 0 and flag1 == 1:
                                                        if z1 == -1:
                                                            stack[0] = le2[i]
                                                        else:
                                                            x = 0; flag = 0; pr_v = -1;
                                                            # найдём приоритет верхушки стэка:
                                                            while x < 5 and flag == 0:
                                                                if prior[x][0] == stack[z1] or prior[x][1] == stack[z1]:
                                                                    flag = 1; pr_v = x;
                                                                else:
                                                                    x = x + 1;
                                                            if pr_v < pr_o:
                                                                flag1 = 0;
                                                                if z1 + 1 < 100:
                                                                    stack[z1 + 1] = le2[i]
                                                            else:
                                                                opz.append(stack[z1]); stack[z1] = ""; z1 = z1 - 1;
                                                    if z1 + 1 < 100:
                                                        stack[z1 + 1] = le2[i];
                                        else:
                                            if le2[i] == "R0":
                                                z = 0
                                                while z < 100 and stack[z] != "":
                                                    z = z + 1;
                                                if z < 100:
                                                    stack[z] = le2[i]
                                            else:
                                                if le2[i] == "R1":
                                                    z = 0
                                                    while z < 100 and stack[z] != "":
                                                        z = z + 1
                                                    z = z - 1
                                                    while z >= 0 and stack[z] != "R0":
                                                        opz.append(stack[z]); stack[z] = ""; z = z - 1;
                                                    if z >= 0:
                                                        if stack[z] == "R0":
                                                            stack[z] = ""
                                                else:
                                                    opz.append(le2[i])
                                    v = 0; fl1 = 0;
                                    while v < 100 and fl1 == 0:
                                        if stack[v] == "":
                                            fl1 = 1
                                        else:
                                            v = v + 1
                                    v = v - 1;
                                    while v >= 0:
                                        opz.append(stack[v]); v = v - 1;
                                    # print(opz) #проверено
                                    # соберём массив числовых констант в итоговом уравнении, чтобы знать, какого порядка числа в нём есть
                                    chisla = []; o = 0;
                                    while ((o < 100) and (N[o] != "")):
                                        chisla.append(int(N[o])); o += 1
                                    if len(chisla) == 0:  # если числа не используются, предполагается, что используются коэффициенты 1 или -1 в зависимости от операции. Например, в уравнении x+y=z<=>x+y-z=0
                                        # Такой вариант гарантирует, что список чисел будет точно непустым, так как в левой части уравнения всегда будет хотя бы одна операция вычитания в связи с переносом правой части исходного уравнения влево
                                        le3 = len(opz)
                                        for i_ in range(le3):
                                            if opz[i_] == "O0":
                                                chisla.append(1)
                                            else:
                                                if opz[i_] == "O1":
                                                    chisla.append(-1)
                                    # print(chisla) #проверено
                                    chisla.sort();
                                    nn = len(chisla);
                                    min_n = chisla[0]; max_n = chisla[nn - 1]; sr = sum(chisla) / nn
                                    if nn % 2 == 0:
                                        med = (chisla[int(nn / 2) - 1] + chisla[int(nn / 2)]) / 2
                                    else:
                                        med = chisla[int((nn + 1) / 2) - 1]
                                    # print(chisla, nn, min_n, max_n, sr, med, end=" #\n") #проверено
                                    """args=[];
                                    for i in range(kper):
                                        args.append(1)
                                    args=[3,7,97];
                                    print(args); print(" # "); print(func(opz,args))"""  # проверено
                                    """nach = time.time()
                                    list1 = gen_nabory(kper, 9)
                                    vsego=len(list1)
                                    ost1=set()
                                    for q in range(vsego):
                                        q1=func(opz,list1[q])%9
                                        ost1.add(q1)
                                    kon = time.time()
                                    dlit = kon - nach
                                    print(ost1); print("&"); print(dlit); print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")"""
                                    ogranich = 0  # по умолчанию нет ограничений на корни уравнения (системы)
                                    err_ogranich = 1  # маркер ошибки в записи ограничений
                                    text_err_ogranich = ""  # текст сообщения об ошибке в записи ограничений
                                    if len(s3) > 0:
                                        ogranich = 1  # уже какие-то ограничения есть, пусть даже и неверно записанные
                                        usl = s3.split(',')  # список ограничений
                                        # print(usl)
                                        n_usl = len(usl)  # число ограничений
                                        for д in range(n_usl):
                                            л = "";
                                            ж = len(usl[д])
                                            for ъ in range(ж):
                                                if usl[д][ъ] != ' ':
                                                    л += usl[д][ъ]
                                            usl[д] = л
                                        # print(usl)
                                        ogr = []
                                        for д in range(n_usl):
                                            ogr.append([])
                                        for д in range(n_usl):
                                            л = ""; ж = len(usl[д]); ъ = 0
                                            while ъ < ж and usl[д][ъ] != '<' and usl[д][ъ] != '>' and usl[д][ъ] != '=':
                                                л += usl[д][ъ];
                                                ъ += 1;
                                            if ъ < ж:
                                                if usl[д][ъ] == '<' or usl[д][ъ] == '>':
                                                    if ъ < ж - 1 and usl[д][ъ + 1] == '=':
                                                        ogr[д].append(usl[д][ъ] + usl[д][ъ + 1])
                                                        ъ += 2
                                                    else:
                                                        ogr[д].append(usl[д][ъ])
                                                        ъ += 1
                                                else:
                                                    if usl[д][ъ] == '=':
                                                        ogr[д].append(usl[д][ъ])
                                                        ъ += 1
                                                if len(л) > 0:
                                                    й = 0
                                                    while й < 100 and I[й] != л:
                                                        й += 1
                                                    if й < 100:
                                                        ogr[д].append(й)
                                                        л1 = ""
                                                        while ъ < ж:
                                                            л1 += usl[д][ъ]
                                                            ъ += 1
                                                        фл = 1; сч = 0; лл1 = len(л1)
                                                        while сч < лл1 and фл == 1:
                                                            if л1[сч] < '0' or л1[сч] > '9':
                                                                фл = 0
                                                            else:
                                                                сч += 1
                                                        if фл == 1 and лл1 > 0:
                                                            ogr[д].append(int(л1))
                                                        else:
                                                            text_err_ogranich = "По крайней мере в одном ограничении неправильно написано число."
                                                    else:
                                                        text_err_ogranich = "По крайней мере в одном ограничении есть переменная, которой нет ни в одном из записанных уравнений."
                                                else:
                                                    text_err_ogranich = "По крайней мере в одном ограничении перед знаком равенства или неравенства ничего не написано."
                                            else:
                                                text_err_ogranich = "По крайней мере в одном ограничении нет знака неравенства или равенства."
                                        if text_err_ogranich == "":
                                            err_ogranich = 0
                                            print(ogr)
                                        else:
                                            print(text_err_ogranich)
                                    # Генетический алгоритм:
                                    start = time.time()  # засекаем время начала работы генетического алгоритма
                                    hrom1 = []  # список хромосом первого поколения
                                    # n1 = int(s1)
                                    for i in range(n1):
                                        hrom1.append([])
                                    for i in range(n1):
                                        for j in range(kper):
                                            hrom1[i].append(random.randint(-10, 10))
                                    for i in range(n1):
                                        if func(opz, hrom1[i]) != 0:  # хромосома мутирует с вероятностью 1, но только если она не является решением уравнения
                                            rg = random.randint(0, kper - 1)  # выбираем случайный мутирующий ген
                                            hrom1[i][rg] = random.randint(-1000, 1000)
                                            if func(opz, hrom1[i]) != 0:  # если после первой мутации хромосома не стала решением уравнения, то проводим вторую мутацию
                                                rg2 = random.randint(0, kper - 1)  # выбираем второй мутирующий ген
                                                if int(med) < int(sr):
                                                    hrom1[i][rg2] = random.randint(int(med), int(sr))
                                                else:
                                                    hrom1[i][rg2] = random.randint(int(sr), int(med))
                                                if func(opz, hrom1[i]) != 0:  # если и вторая мутация не помогла, то проводим третью мутацию
                                                    rg3 = random.randint(0, kper - 1)
                                                    hrom1[i][rg3] = random.randint(-5, 5)
                                    flag2 = 0
                                    resh = []  # список найденных решений
                                    for i in range(n1):
                                        if func(opz, hrom1[i]) == 0:
                                            resh.append(hrom1[i])
                                        if func(opz, hrom1[i]) != None:
                                            flag2 = 1
                                    re1 = to_set(resh)
                                    n2 = int(n1 * (n1 - 1) / 2)
                                    hrom2 = [];  # список хромосом второго поколения
                                    for i in range(n2):
                                        hrom2.append([])
                                    h = 0
                                    for i in range(n1):
                                        for j in range(i + 1, n1):
                                            t = random.randint(0, kper - 2)
                                            for j1 in range(t):
                                                hrom2[h].append(hrom1[i][j1])
                                            for j1 in range(t, kper):
                                                hrom2[h].append(hrom1[j][j1])
                                            h = h + 1
                                    # print(hrom2)
                                    for i in range(n2):
                                        if func(opz, hrom2[i]) != 0:
                                            rg = random.randint(0, kper - 1)  # выбираем случайный мутирующий ген
                                            hrom2[i][rg] = random.randint(-1000, 1000)
                                            if func(opz, hrom2[i]) != 0:
                                                rg2 = random.randint(0, kper - 1)  # выбираем второй мутирующий ген
                                                if int(med) < int(sr):
                                                    hrom2[i][rg2] = random.randint(int(med), int(sr))
                                                else:
                                                    hrom2[i][rg2] = random.randint(int(sr), int(med))
                                                if func(opz, hrom2[i]) != 0:
                                                    rg3 = random.randint(0, kper - 1)
                                                    hrom2[i][rg3] = random.randint(-5, 5)
                                    for i in range(n2):
                                        if func(opz, hrom2[i]) == 0:
                                            resh.append(hrom2[i])
                                        if func(opz, hrom2[i]) != None:
                                            flag2 = 1
                                    re2 = to_set(resh)
                                    ge = 2  # число уже сгенерированных поколений
                                    flag_ = 2
                                    if re1 == re2 and re1 != []:
                                        flag_ = 1
                                    else:
                                        flag_ = 0
                                    # max_gen = int(s2)
                                    while ge <= max_gen and flag_ == 0:
                                        re1 = re2; hrom_ = []; n_ = int(n1 * (n1 - 1) / 2)
                                        for i in range(n_):
                                            hrom_.append([])
                                        h = 0
                                        for i in range(n1):
                                            for j in range(i + 1, n1):
                                                t = random.randint(0, kper - 2)
                                                for j1 in range(t):
                                                    hrom_[h].append(hrom2[i][j1])
                                                for j1 in range(t, kper):
                                                    hrom_[h].append(hrom2[j][j1])
                                                h = h + 1
                                        # проведём мутацию в очередном поколении в ~mut доли случаев
                                        for i in range(n_):
                                            if func(opz, hrom_[i]) != 0:
                                                rg = random.randint(0, kper - 1)  # выбираем случайный мутирующий ген
                                                hrom_[i][rg] = random.randint(-1000, 1000)
                                                if func(opz, hrom_[i]) != 0:
                                                    rg2 = random.randint(0, kper - 1)  # выбираем второй мутирующий ген
                                                    if int(med) < int(sr):
                                                        hrom_[i][rg2] = random.randint(int(med), int(sr))
                                                    else:
                                                        hrom_[i][rg2] = random.randint(int(sr), int(med))
                                                    if func(opz, hrom_[i]) != 0:
                                                        rg3 = random.randint(0, kper - 1)
                                                        hrom_[i][rg3] = random.randint(-5, 5)
                                        for i in range(n_):
                                            if func(opz, hrom_[i]) == 0:
                                                resh.append(hrom_[i])
                                            if func(opz, hrom_[i]) != None:
                                                flag2 = 1
                                        re2 = to_set(resh)
                                        if re1 == re2 and re1 != []:
                                            flag_ = 1
                                        else:
                                            ge = ge + 1
                                        hrom2 = hrom_
                                    res_s = ""
                                    if ogranich == 0 or err_ogranich == 1:
                                        for i in range(len(re2)):
                                            stro = "";
                                            for j in range(kper):
                                                stro = stro + I[j] + "=" + str(re2[i][j]) + "\n"
                                            res_s = res_s + stro + "\n"
                                    else:  # в этом случае есть ограничения, написанные без ошибок. Нужно обработать этот случай.
                                        for i in range(len(re2)):
                                            flag_ogr = 1;
                                            ц = 0
                                            while ц < n_usl and flag_ogr == 1:
                                                if ogr[ц][0] == '<':
                                                    if re2[i][ogr[ц][1]] >= ogr[ц][2]:
                                                        flag_ogr = 0
                                                if ogr[ц][0] == '>':
                                                    if re2[i][ogr[ц][1]] <= ogr[ц][2]:
                                                        flag_ogr = 0
                                                if ogr[ц][0] == '=':
                                                    if re2[i][ogr[ц][1]] != ogr[ц][2]:
                                                        flag_ogr = 0
                                                if ogr[ц][0] == '<=':
                                                    if re2[i][ogr[ц][1]] > ogr[ц][2]:
                                                        flag_ogr = 0
                                                if ogr[ц][0] == '>=':
                                                    if re2[i][ogr[ц][1]] < ogr[ц][2]:
                                                        flag_ogr = 0
                                                if flag_ogr == 1:
                                                    ц += 1
                                            if flag_ogr == 1:
                                                stro = "";
                                                for j in range(kper):
                                                    stro = stro + I[j] + "=" + str(re2[i][j]) + "\n"
                                                res_s = res_s + stro + "\n"
                                    finish = time.time()  # засекаем время окончания работы генетического алгоритма
                                    ti = finish - start  # время выполнения генетического алгоритма
                                    if len(re2) > 0:
                                        count += 1; summa += ti; sred = summa / count; count1 += 1;
                                        if ti > maxti:
                                            maxti = ti;
                                        if ogranich == 1 and err_ogranich == 0:
                                            if res_s == "":
                                                textView2.insert("1.0",
                                                                 "Не нашлось решений, удовлетворяющих заданным ограничениям, но нашлись другие решения." + "\n" + "Время выполнения генетического алгоритма: " + str(
                                                                     ti) + " секунды.\nСреднее время выполнения: " + str(
                                                                     sred) + " секунды.\nПрограмму запускали " + str(
                                                                     count) + " раз.\nМаксимальное время выполнения: " + str(
                                                                     maxti) + " секунды. Хотя бы 1 решение нашлось в " + str(
                                                                     count1) + " случаях.")
                                            else:
                                                textView2.insert("1.0",
                                                                 "Найденные решения, удовлетворяющие указанным ограничениям:\n" + res_s + "\n" + "Время выполнения генетического алгоритма: " + str(
                                                                     ti) + " секунды.\nСреднее время выполнения: " + str(
                                                                     sred) + " секунды.\nПрограмму запускали " + str(
                                                                     count) + " раз.\nМаксимальное время выполнения: " + str(
                                                                     maxti) + " секунды. Хотя бы 1 решение нашлось в " + str(
                                                                     count1) + " случаях.")
                                        else:
                                            if ogranich == 1 and err_ogranich == 1:
                                                textView2.insert("1.0",
                                                                 text_err_ogranich + "\n" + "Найденные решения:\n" + res_s + "\n" + "Время выполнения генетического алгоритма: " + str(
                                                                     ti) + " секунды.\nСреднее время выполнения: " + str(
                                                                     sred) + " секунды.\nПрограмму запускали " + str(
                                                                     count) + " раз.\nМаксимальное время выполнения: " + str(
                                                                     maxti) + " секунды. Хотя бы 1 решение нашлось в " + str(
                                                                     count1) + " случаях.")
                                            else:
                                                textView2.insert("1.0",
                                                                 "Найденные решения:\n" + res_s + "\n" + "Время выполнения генетического алгоритма: " + str(
                                                                     ti) + " секунды.\nСреднее время выполнения: " + str(
                                                                     sred) + " секунды.\nПрограмму запускали " + str(
                                                                     count) + " раз.\nМаксимальное время выполнения: " + str(
                                                                     maxti) + " секунды. Хотя бы 1 решение нашлось в " + str(
                                                                     count1) + " случаях.")
                                        # textView2.insert("3.0","Время выполнения генетического алгоритма: "+str(ti)+" секунды.")
                                    else:
                                        if ogranich == 1 and err_ogranich == 0:
                                            textView2.insert("1.0", "К сожалению, никаких решений не нашлось.")
                                        else:
                                            if ogranich == 1 and err_ogranich == 1:
                                                textView2.insert("1.0",text_err_ogranich + "\n" + "К сожалению, никаких решений не нашлось.")
                                            else:
                                                textView2.insert("1.0", "К сожалению, решений не нашлось.")
                                        textView2.insert("2.0", "\n")
                                        textView2.insert("3.0", "Время выполнения генетического алгоритма: " + str(ti) + " секунды.")
                                        textView2.insert("4.0", "\n");
                                        count += 1;
                                        summa += ti;
                                        sred = summa / count;
                                        if ti > maxti:
                                            maxti = ti;
                                        textView2.insert("5.0", "Среднее время выполнения: " + str(sred) + " секунды.")
                                        textView2.insert("6.0", "\n")
                                        textView2.insert("7.0", "Программу запускали " + str(count) + " раз.")
                                        textView2.insert("8.0", "\n")
                                        textView2.insert("9.0", "Максимальное время выполнения программы: " + str(maxti) + " секунды.")
                                        textView2.insert("10.0","Хотя бы 1 решение нашлось в " + str(count1) + " случаях.")
                            else:
                                textView2.insert("1.0", "Параметры генетического алгоритма должны быть натуральными числами.")
                        else:
                            textView2.insert("1.0", "В уравнении или системе одна переменная (а должно быть более одной переменной) или какой-то из параметров генетического алгоритма введён неверно (параметры должны быть натуральными числами).")
                    else:
                        textView2.insert("1.0", "Левая часть некоторых записанных уравнений отсутствует.")
                else:
                    textView2.insert("1.0", "Правая часть некоторых записанных уравнений отсутствует.")
            else:
                textView2.insert("1.0", "В некоторых записанных уравнениях содержится не один знак равенства.")
        else:
            textView2.insert("1.0", "Лексический анализ уравнения или системы уравнений прошёл с ошибками.")


    button = tk.Button(text="Готово", command=ONCLICK)
    textView2 = tk.Text()
    button.pack()
    textView2.pack()
    """editText.insert(0,"x+y=1616,x+2*y=2325,x+3*y=3034,x+4*y=3743,x+5*y=4452,x+6*y=5161,x+7*y=5870,x+8*y=6579,x+9*y=7288,x+10*y=7997")
    et1.insert(0,"45")
    et2.insert(0,"300")
    for ё in range(2):
        ONCLICK()"""
    window.mainloop()
    # В уравнении x^2+y^2=z*(x+y) куда-то девает последнюю операцию вычитания (ошибка в переводе в ОПЗ)!!!
    # Для вышеуказанного уравнения получается I0 N0 O4 I1 N0 O4 O0 I2 I0 I1 O0 O2
    #print_hi('PyCharm')
#print(77093**77093)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
