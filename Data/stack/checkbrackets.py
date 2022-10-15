"""
检查一段文件里的括号是否成对出现
"""
# import Data.stack.sstack
import sstack
#遍历这段文字，如果碰到"（{[",入栈，判断到“）}]”,则出栈
#判断出栈的元素是否与检查到元素成对

txt = """adadfaa(dadsf[adfdc]a,dadfd--{dadiickks,sdfaf(dkll))})"""
bracket_parens = "(){}[]" #验证的内容
bracket_lift = ["(","{","["]
dict_bracket = {")":"(","}":"{","]":"["}#对应关系

def checkbracket(txt):
    # i = 0
    # txt_len = len(txt)
    #开发者约定俗称的定义方式
    i,txt_len = 0,len(txt)
    while True:
        #逐个遍历字符串，如果没有到结尾并且不是括号，就向后遍历
        while i < txt_len and txt[i] not in bracket_parens:
            i += 1
        #两种条件循环，出来后要判断是那种情况退出循环。
        #遍历到了结尾
        if i >= txt_len:
            return
        else:
            #生成器返回括号字符和对应的位置，还不熟悉，要重新看一下
            yield txt[i],i
            #去到下一个字符
            i += 1


#初始化一个栈
st = sstack.SStack()
#遍历返回的值
for pr,i in checkbracket(txt):
    if pr in bracket_lift:
        #将左括号和位置信息入栈
        st.push((pr,i))
    #如果是空的，或者匹配的不正确，报错
    elif st.is_empty() or st.pop()[0] != dict_bracket[pr]:
        print("unmatching is found at %d for %s"%(i,pr))
        break
else:
    #循环正常结束，判断栈是否为空
    if st.is_empty():
        print("All brackets are matched")
    else:
        e = st.pop()
        print("unmatching is found at %d for %s"%(e[1],e[0]))

