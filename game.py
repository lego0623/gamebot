import asyncio,discord,os
from discord import message
from discord import channel
from discord.ext import commands
from discord.utils import deprecated
import time
# import random

game = discord.Game("!!명령어 입력")
bot = commands.Bot(command_prefix='!!',Status = discord.Status.online, activity = game, help_command = None)
mafia_game_ready = False
mafia_gameing = False
mafia_game_count = 0
if(True): # 끝말잇기 변수
    end_bind_ready = []
    end_binding = []
    end_bind_user = []
    end_bind_end = []
    end_bind_list = [] # 리스트
    end_bind_time = []
    end_bind_score = []
if(True): # 숫자야구 변수
    num_base_ready = []
    num_baseing = []
    num_base_user = []
    num_base_score = []
    num_base_home = []

game = discord.Game("@@명령어 입력!")
bot = commands.Bot(command_prefix='@@',Status=discord.Status.online,activity=game,help_command=None)
prefix = "@@"

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",".","?","!","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","_"]

with open(r'C:\Users\owner\Documents\GitHub\gamebot\words.txt', 'r', encoding='UTF8') as f:
    data = f.read()
file_list = data.splitlines()

@bot.event
async def on_ready():
    print("마이야히 마이야하")
    await message.channel.send("뿜!")

if(True):
    bad = ['ㅅㅂ','시발','씨발',"시바", "새끼", "병신", "ㅅㄲ","ㅂㅅ","새1끼", "씨1발","병1신","시1발","시1바"] 
@bot.event
async def on_message(message): ##### remove bad words 
    if(True): # 필터
        message_contant=message.content 
        for i in bad: 
            if i in message_contant: 
                if message.author.dm_channel:
                    await message.author.dm_channel.send("욕 좀 고마해라")
                elif message.author.dm_channel is None:
                    channel = await message.author.create_dm()
                    await channel.send("욕 좀 고마해라")
                await message.channel.send('욕 필터링 ㅅㄱ') 
                await message.delete()
    if(True):
        global num_base_ready
        global num_baseing
        global num_base_user
        global num_base_score
        global num_base_home
        if(message.content == "" + prefix +"숫자야구_시작"):
            print("sfgf")
            if(not message.author in num_base_user): #not num_baseing
                num_base_user.append(message.author)
                user_id_base = num_base_user.index(message.author) 
                num_base_user.append(message.author)
                num_baseing.append(True)
                num_base_score.append(0)
                num_base_home.append("")
                msg = await message.channel.send("숫자야구를 시작합니다(3자리 숫자)")
                while(not len(num_base_home[user_id_base])==3):
                    ab = str(random.randrange(0,10))
                    if(len(num_base_home[user_id_base]) == 0):
                        num_base_home[user_id_base] = num_base_home[user_id_base] + ab
                        print(ab)
                    if(len(num_base_home[user_id_base]) == 1):
                        if(not(ab == num_base_home[user_id_base][0])):
                            num_base_home[user_id_base] = num_base_home[user_id_base] + ab
                            print(ab)
                    if(len(num_base_home[user_id_base]) == 2):
                        if(not(ab == num_base_home[user_id_base][0] or ab == num_base_home[user_id_base][1])):
                            num_base_home[user_id_base] = num_base_home[user_id_base] + ab
                            print(ab)
                print(num_base_home[user_id_base])
                
        if(message.content.startswith("@@ㄹ ")):
            if(message.author in num_base_user):
                user_id_base = num_base_user.index(message.author)
                print(str(num_base_score),str(user_id_base))
                if(message.content == "@@ㄹ !포기!"):
                    await message.channel.send("당신이 졌습니다. /" + str(num_base_score[int(user_id_base)]) + "회 만에 항복")
                    del num_baseing[user_id_base]
                    del num_base_user[user_id_base]
                    del num_base_score[user_id_base]
                    del num_base_home[user_id_base]
                else:
                    sbo = ""
                    try:
                        print(message.content[4:7])
                        if(int(message.content[4:7])):
                            pass
                        print("a1")
                        for i in range(0,len(num_base_home[user_id_base])):
                            print("a2")
                            if(message.content[i+4] == num_base_home[user_id_base][i]):
                                sbo = sbo + "S"
                            if(message.content[i+4] != num_base_home[user_id_base][i]):
                                ag = False
                                for jk in range(0,len(num_base_home[user_id_base])):
                                    if(message.content[i+4] == num_base_home[user_id_base][jk]):
                                        sbo = sbo + "B"
                                        ag = True
                                if(not ag):
                                    sbo = sbo + "N"
                        print("a3")
                        if(sbo == "NNN"):
                            await message.channel.send("" + message.content[4:7] + ", 0스트라이크/0볼/아웃!")
                            num_base_score[int(user_id_base)] = int(num_base_score[int(user_id_base)])+1
                        elif(sbo == "SSS"):
                            await message.channel.send("" + message.content[4:7] + ", 3스트라이크/0볼! " + str(num_base_score[user_id_base]) + "회만에 게임 승리!")
                            del num_baseing[user_id_base]
                            del num_base_user[user_id_base]
                            del num_base_score[user_id_base]
                            del num_base_home[user_id_base]
                            print("r")
                        elif(sbo == "BBB"):
                            print("r23")
                            await message.channel.send("" + message.content[4:7] + ", 0스트라이크/3볼")
                            num_base_score[int(user_id_base)] = int(num_base_score[int(user_id_base)])+1
                        elif(not sbo == "NNN" and not sbo == "SSS" and not sbo == "BBB"):
                            print("r2")
                            strike = 0
                            ball = 0
                            for jklo in range(0, len(sbo)):
                                if(sbo[jklo] == "S"):
                                    strike += 1
                                if(sbo[jklo] == "B"):
                                    ball += 1
                            await message.channel.send("" + message.content[4:7] + ", " + str(strike) + "스트라이크/" + str(ball) + "볼")
                            num_base_score[int(user_id_base)] = int(num_base_score[int(user_id_base)])+1
                    except:
                        await message.channel.send("@@ㄹ (숫자)로 적어주십시오(숫자는 3자리 숫자입니다. (예:@@ㄹ 123))")
    if(True): # 끝말잇기
        global end_bind_end
        global end_bind_list
        global end_bind_ready
        global end_bind_user
        global end_binding
        global end_bind_time
        global end_bind_score
        if(message.content.startswith('' + prefix + '끝말잇기_시작') and not message.author in end_bind_user):
            msg = await message.channel.send("끝말잇기가 5초 뒤에 시작합니다.")
            for i in range(0, 4):
                time.sleep(1)
                await msg.edit(content='끝말잇기가 ' + str(4-i) + '초 뒤에 시작합니다.')
            time.sleep(1)
            await msg.edit(content='끝말잇기가 시작합니다.')
            end_binding.append(True)
            end_bind_time.append(True)
            end_bind_user.append(str(message.author))
            first_word = file_list[random.randrange(0, len(file_list))]
            # random.range()
            await message.channel.send("제시어: " + first_word + "")
            await message.channel.send("" + str(message.author) + "님 시작 단어(" + first_word[len(first_word)-1] + ")") 
            end_bind_end.append(first_word)
        if(message.content.startswith("" + prefix + "ㅇ")):
            print(str(message.content))
            # print(end_bind_end)
            print(str(message.content[len(str(message.content))-1]))
            aghdg = []
            if(message.author in end_bind_user):
                user_id_base2 = end_bind_user.index(message.author)
                if(end_binding[user_id_base2]):
                    if(str(message.content) == "" + prefix + "ㅇ !포기!"):
                        if(end_bind_time[user_id_base2]):
                            await message.channel.send(content='당신이 졌군요 /' + str(end_bind_score[user_id_base2]) + '점/패배')
                            del end_bind_ready[user_id_base2]
                            del end_binding[user_id_base2]
                            del end_bind_user
                            del end_bind_end
                            del end_bind_list
                            del end_bind_time
                            del end_bind_score
                    else:
                        if(str(message.content[4]) == end_bind_end[user_id_base2][len(end_bind_end)-1] and str(message.author) == end_bind_user[user_id_base2]):
                            print("asdfds")
                            if(message.content[4:len(message.content)] in file_list and not message.content[4:len(message.content)] in end_bind_list[user_id_base2]):
                                end_bind_time[user_id_base2] = False
                                end_bind_score[user_id_base2] += 1
                                for ggg in range(0, len(file_list)):
                                    if(message.content[len(message.content)-1] == file_list[ggg][0]):
                                        aghdg.append(file_list[ggg])
                                end_bind_end[user_id_base2] = aghdg[random.randrange(0, len(aghdg))]
                                end_bind_list[user_id_base2].append(end_bind_end[user_id_base2])
                                print(end_bind_list[user_id_base2])
                                try:
                                    await message.channel.send("" + end_bind_end[user_id_base2] + ", " + str(message.author) + "님 시작 단어(" + end_bind_end[user_id_base2][len(end_bind_end[user_id_base2])-1] + ")") 
                                    print(end_bind_end[user_id_base2])
                                    msg = await message.channel.send("10초 남음")
                                    end_bind_time[user_id_base2] = True
                                    for ijk in range(0, 10):
                                        if(end_bind_time[user_id_base2]):
                                            time.sleep(1)
                                        if(end_bind_time[user_id_base2]):
                                            await msg.edit(content='' + str(10-ijk) + '초 남음')
                                    if(end_bind_time[user_id_base2]):
                                        time.sleep(1)
                                    if(end_bind_time[user_id_base2]):
                                        await msg.edit(content='당신이 졌군요 /' + str(end_bind_score[user_id_base2]) + '점/패배')
                                        del end_bind_ready[user_id_base2]
                                        del end_binding[user_id_base2]
                                        del end_bind_user
                                        del end_bind_end
                                        del end_bind_list
                                        del end_bind_time
                                        del end_bind_score 
                                except:
                                    await message.msg.edit("워우...제가 졌군요... /" + str(end_bind_score[user_id_base2]) + "점/승리")
                                    del end_bind_ready[user_id_base2]
                                    del end_binding[user_id_base2]
                                    del end_bind_user
                                    del end_bind_end
                                    del end_bind_list
                                    del end_bind_time
                                    del end_bind_score
    # if(True): # 복불복
    #     if(message.content.startswith('' + prefix + '복불복 ')):
    #         try:
    #             if(int(message.content[6:len(message.content)])):
    #                 pass
    #             total = int(message.content[6:len(message.content)])
    #             if(random.randrange(0, total) == 0):
    #                 await message.channel.send("당첨되셨습니다!")
    #             else:
    #                 await message.channel.send("꽝!")
    #         except:
    #             await message.channel.send("* @@복불복 (숫자)의 형태로 적어주세요. (확률: 1/(숫자))")
    if(message.content == "" + prefix + "도움_명령어"):
        embed = discord.Embed(title=f"명령어", descriotion=f"도리도리봇", Color=0xf3bb76)
        embed.add_field(name=f"-" + prefix + "끝말잇기_규칙",value=f"끝말잇기 규칙", inline=False)
        embed.add_field(name=f"-" + prefix + "끝말잇기_게임방법",value=f"끝말잇기 게임방법", inline=False)
        embed.add_field(name=f"-" + prefix + "숫자야구_규칙",value=f"숫자야구 규칙", inline=False)
        embed.add_field(name=f"-" + prefix + "숫자야구_게임방법",value=f"숫자야구 게임방법", inline=False)
        await message.channel.send(embed=embed)
    if(message.content == "" + prefix + "숫자야구_게임방법"):
        embed = discord.Embed(title=f"숫자야구_사용방법", descriotion=f"도리도리봇", Color=0xf3bb76)
        embed.add_field(name=f"-" + prefix + "숫자야구_시작",value=f"숫자야구를 시작한다. (AI)", inline=False)
        embed.add_field(name=f"-" + prefix + "ㄹ",value=f"" + prefix + "ㄹ (숫자)로 여부를 알수 있다.", inline=False)
        embed.add_field(name=f"-" + prefix + "ㄹ !포기!",value=f"숫자야구에서 항복을 요청한다.", inline=False)
    if(message.content == "" + prefix + "숫자야구_규칙"):
        embed = discord.Embed(title=f"숫자야구_규칙", descriotion=f"도리도리봇", Color=0xf3bb76)
        embed.add_field(name=f"규칙 (1)",value=f"숫자는 3자리 수임(000~999)", inline=False)
        embed.add_field(name=f"규칙 (2)",value=f"제한 시간은 없음", inline=False)
        embed.add_field(name=f"게임규칙 (1)",value=f"숫자가 정답숫자의 포함되어있으면 1볼(예: (정답: 1xx), (자신의 답: x1x))", inline=False)
        embed.add_field(name=f"게임규칙 (2)",value=f"숫자가 정답숫자의 포함되어있고 위치도 같으면 1스트라이크(예: (정답: 1xx), (자신의 답: 1xx))", inline=False)
        embed.add_field(name=f"게임규칙 (3)",value=f"숫자가 정답숫자의 포함되어있지않으면 없음(만일 3가지 숫자다 없을 경우 아웃(예: (정답: 123), (자신의 답: 456))", inline=False)
        embed.add_field(name=f"게임규칙 (4)",value=f"모든 숫자의 위치가 같으면 3스트라이크 즉 게임 승(예: (정답: 123), (자신의 답: 123))", inline=False)
    if(message.content == "" + prefix + "끝말잇기_게임방법"):
        embed = discord.Embed(title=f"끝말잇기_사용방법", descriotion=f"도리도리봇", Color=0xf3bb76)
        embed.add_field(name=f"-" + prefix + "끝말잇기_시작",value=f"끝말잇기를 시작한다. (AI)", inline=False)
        embed.add_field(name=f"-" + prefix + "ㅇ",value=f"" + prefix + "ㅇ (단어)로 끝말잇기를 이어갈 수 있다.", inline=False)
        embed.add_field(name=f"-" + prefix + "ㅇ !포기!",value=f"끝말잇기에서 항복을 요청한다.", inline=False)
    if(message.content == "" + prefix + "끝말잇기 규칙"):
        embed = discord.Embed(title=f"끝말잇기_규칙", descriotion=f"도리도리봇", Color=0xf3bb76)
        embed.add_field(name=f"규칙 (1)",value=f"제시된 단어의 끝말을 잇는 단어를 말한다.", inline=False)
        embed.add_field(name=f"규칙 (2)",value=f"제한시간은 10초이다.", inline=False)
        embed.add_field(name=f"유의사항",value=f"단어가 봇의 데이터에 없을 수도 있다. 그럴때는 억울해 하면된다.", inline=False)

def password2():
    a = "01011010100010011001100110100101100011001001011110111101010110101100100110011011101101011000001010001111101111000101100001101000111110111110010101101100100001011011100100111000110111010101101101011000011000000101011110011100000100000001110010000000010100010110000100000101100010100111101011001000100100101101000011000110010111101011001001110100001101011010000010000010001001011101000010000001010001100010100101011"
    b = 0
    c = ""
    d = int(len(a)/7)

    for i in range(0, d):
        b = 0
        for j in range(i*7, i*7+7):
            if(a[j] == "1"):
                b = b*2+1
            elif(a[j] == "0"):
                b = b*2
        c = c+alphabet[b-1]
    bot.run(c)
password2()