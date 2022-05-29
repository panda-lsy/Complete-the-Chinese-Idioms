import random
import easygui as g
import json 

level=0
score=0
health=3
help=5
exit=False

source_word=[]                                              #词语字典     
source_meaning=[]                                           #意义字典   
source_derivation=[]                                        #出处字典
source_example=[]                                           #使用例字典
source_pinyin=[]                                            #拼音字典
with open('idiom.json','r',encoding='utf8')as fp:           #打开JSON
    json_data = json.load(fp)
    for i in range(0,len(json_data)-1):                     #循环遍历json_data数据
        #print(i)                                            #!输出测试
        #print(json_data[i]["word"])                         #!输出测试
        source_word.append(json_data[i]["word"].replace("，",""))            #加入到词语字典里
        source_meaning.append(json_data[i]["explanation"])  #加入到意义字典里
        source_derivation.append(json_data[i]["derivation"])#加入到出处字典里
        source_example.append(json_data[i]["example"])      #加入到使用例字典里
        source_pinyin.append(json_data[i]["pinyin"])        #加入到拼音字典里
            
#print(source_word)                                          #!输出测试       
#print(source_meaning)                                           
#print(source_derivation)  
#print(source_example) 
#print(source_pinyin)                                                         

while True:
    if exit==True:
        break
    if health<=0:
        g.ynbox(msg='你已经没有生命了！', title='生命不足', choices=('[<F1>]好的', '[<F2>]不'), image=None, default_choice='[<F1>]好的')
        break
    if score<0:
        g.ynbox(msg='你已经没有分数了！', title='分数不足', choices=('[<F1>]好的', '[<F2>]不'), image=None, default_choice='[<F1>]好的')
        break
    word=random.choice(source_word)#从词语列表中随机选择一个成语word
    blank=random.choice(word)#从选出的成语word中随机选一个字作为要填的空blank
    ques=word.replace(blank,"_")#将要填的空blank替换为__,形成题目ques
    a=random.randint(1,5)
    #print(a)
    if a==1:
        choice1=blank
        choice2=random.choice(random.choice(source_word))
        choice3=random.choice(random.choice(source_word))
        choice4=random.choice(random.choice(source_word))
    elif a==2:
        choice2=blank
        choice1=random.choice(random.choice(source_word))
        choice3=random.choice(random.choice(source_word))
        choice4=random.choice(random.choice(source_word))
    elif a==3:
        choice3=blank
        choice1=random.choice(random.choice(source_word))
        choice2=random.choice(random.choice(source_word))
        choice4=random.choice(random.choice(source_word))
    elif a==4:
        choice4=blank
        choice2=random.choice(random.choice(source_word))
        choice3=random.choice(random.choice(source_word))
        choice1=random.choice(random.choice(source_word))
    pos=source_word.index(word)
    example_tip=False
    meaning_tip=False
    while True:
        knowledge=word+'('+source_pinyin[pos]+')\n'+"意思:"+source_meaning[pos]+"\n"+"使用例:"+source_example[pos]+"\n出处:"+source_derivation[pos]+"\n"
        if example_tip == False and meaning_tip == False:
            answer=g.buttonbox(msg="请填空:\t"+ques, title='第'+str(level+1)+'关\t\t'+"分数:"+str(score)+"❤"*health, choices=(choice1, choice2, choice3, choice4,"更多选项"))#输出题目ques
        elif example_tip == True and meaning_tip == False:
            answer=g.buttonbox(msg="请填空:\t"+ques+"\n提示:\n"+"使用例:"+source_example[pos], title='第'+str(level+1)+'关\t\t'+"分数:"+str(score)+"❤"*health, choices=(choice1, choice2, choice3, choice4,"更多选项"))
        elif example_tip == False and meaning_tip == True:
            answer=g.buttonbox(msg="请填空:\t"+ques+"\n提示:\n"+"意思:"+source_meaning[pos], title='第'+str(level+1)+'关\t\t'+"分数:"+str(score)+"❤"*health, choices=(choice1, choice2, choice3, choice4,"更多选项"))
        elif example_tip == True and meaning_tip == True:
            answer=g.buttonbox(msg="请填空:\t"+ques+"\n提示:\n"+"意思:"+source_meaning[pos]+"使用例:"+source_example[pos], title='第'+str(level+1)+'关\t\t'+"分数:"+str(score)+"❤"*health, choices=(choice1, choice2, choice3, choice4,"更多选项"))
        if answer=="更多选项":
            option=g.buttonbox(msg="你还有"+str(help)+"次提示机会",title="更多选项 分数:"+str(score)+"❤"*health, choices=("跳过本题", "使用例提示", "意义提示","退出游戏","返回"))
            if option=="跳过本题":
                if help-2>=0:
                    g.textbox(msg='正确答案是'+word+'\n'+knowledge, title='跳过本题', text='', codebox=False, callback=None, run=True)
                    level+=1
                    help-=2
                    break
                if help-2<0:
                    g.ynbox(msg="你的提示次数不够了(<2)", title='次数不够', choices=('[<F1>]好的','[<F2>]不好'), image=None, default_choice='[<F1>]好的')
            if option=="意义提示":
                if meaning_tip== False:
                    if help-1>=0:
                        meaning_tip = True
                        help-=1
                    else:
                        g.ynbox(msg="你的提示次数不够了(<1)", title='次数不够', choices=('[<F1>]好的','[<F2>]不好'), image=None, default_choice='[<F1>]好的')
                else:
                    g.ynbox(msg="已经提示过了", title='提示过了', choices=('[<F1>]好的','[<F2>]不好'), image=None, default_choice='[<F1>]好的')
            if option=="使用例提示":
                if example_tip== False:
                    if help-1>=0:
                        example_tip = True
                        help-=1
                    else:
                        g.ynbox(msg="你的提示次数不够了(<1)", title='次数不够', choices=('[<F1>]好的','[<F2>]不好'), image=None, default_choice='[<F1>]好的')
                else:
                    g.ynbox(msg="已经提示过了", title='提示过了', choices=('[<F1>]好的','[<F2>]不好'), image=None, default_choice='[<F1>]好的')
            if option=="退出游戏":
                g.ynbox(msg="游戏结束", title='提示过了', choices=('[<F1>]好的','[<F2>]不好'), image=None, default_choice='[<F1>]好的')
                exit=True
                break
        if answer==blank:
            g.textbox(msg="恭喜,回答正确,加10分"+'\n'+knowledge, title='回答正确', text='', codebox=False, callback=None, run=True)
            score=score+10
            level+=1  
            break
        elif not answer =="更多选项":
            g.textbox(msg="很遗憾,回答错误,减10分,正确答案是"+word+'\n'+knowledge, title='回答错误', text='', codebox=False, callback=None, run=True)
            score=score-10 
            level+=1 
            health-=1
            break
    
g.ynbox(msg="游戏结束,您的最终得分："+str(score)+"\n玩到了第"+str(level)+"关", title='游戏结束', choices=('[<F1>]好的','[<F2>]不好'), image=None, default_choice='[<F1>]好的')


