import subprocess
def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Ausführen des Befehls: {e}")

def main():
    command1 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -T 24  -s 3 --width 576 --height 384 -f 6 -pfx 1 -n "fast camera movement" '
    run_command(command1)

    command2 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -T 24  -s 3 --width 576 --height 384 -f 6 -pfx 2 -n "fast camera movement" '
    run_command(command2)

    command3 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -T 24  -s 3 --width 576 --height 384 -f 6 -pfx 3 -n "fast camera movement" '
    run_command(command3)

    command4 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -T 24  -s 3 --width 576 --height 384 -f 6 -pfx 4 -n "fast camera movement" '
    run_command(command4)

    command5 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -T 24  -s 3 --width 576 --height 384 -f 6 -pfx 5 -n "fast camera movement" '
    run_command(command5)

    command6 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -T 24  -s 3 --width 576 --height 384 -f 6 -pfx 6 -n "fast camera movement" '
    run_command(command6)

    command7 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -T 24  -s 3 --width 576 --height 384 -f 6 -pfx 7 -n "fast camera movement" '
    run_command(command7)

    command8 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 8  '
    run_command(command8)

    command9 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 9 '
    run_command(command9)

    command10 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 10 '
    run_command(command10)
    
    command11 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 11 -s 3'
    run_command(command11)

    command12 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 12 -s 3 '
    run_command(command12)

    command13 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 13 -s 3'
    run_command(command13)

    command14 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 14 -s 40'
    run_command(command14)

    command15 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 15 -s 40 '
    run_command(command15)

    command16 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 16 '
    run_command(command16)

    command17 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping"  -T 24  -s 3 -pfx 17 '
    run_command(command17)  

    command18 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 18 '
    run_command(command18)

    command19 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 19 '
    run_command(command19)

    command20 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 20 '
    run_command(command20)

    command21 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 21 '
    run_command(command21)

    command22 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 22 '
    run_command(command22)

    command23 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "man in a hat, close up on the face" -n "fast character movement, running , jumping"  -T 24  -s 3  -pfx 23 '
    run_command(command23)

    command24 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "close up of a cowboy on a horse" -n "fast character movement, running , jumping"  -T 24  -s 3  -pfx 24 '
    run_command(command24)

    command25 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "close up of a cowboy on a horse" -n "fast character movement, running , jumping"  -T 24  -s 3  -pfx 25 '
    run_command(command25)

    command26 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "close up of a cowboy on a horse" -n "fast character movement, running , jumping"   -T 24  -s 3  -pfx 26 '
    run_command(command26)

    command27 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "close up of a cowboy on a horse" -n "fast character movement, running , jumping"   -T 24  -s 3  -pfx 27 '
    run_command(command27)

    command28 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "close up of a cowboy on a horse" -n "fast character movement, running , jumping"   -T 24  -s 3  -pfx 28 '
    run_command(command28)

    command29 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "close up of a cowboy on a horse" -n "fast character movement, running , jumping"   -T 24  -s 3  -pfx 29 '
    run_command(command29)

    command30 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "close up of a cowboy on a horse, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 30 '
    run_command(command30)
    
    command31 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 31 '
    run_command(command31)

    command32 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command32)


    command33 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command33)

    command34 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command34)

    command35 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 35 '
    run_command(command35)

    command36 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command36)

    command37 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command37)

    command38 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command38)

    command39 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command39)

    command40 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 40 '
    run_command(command40)

    command41 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 41 '
    run_command(command41)

    command42 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n man in a hat, close up on the face" -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 2  '
    run_command(command42)

    command43 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 3 '
    run_command(command43)

    command44 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 4 '
    run_command(command44)

    command45 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 5 '
    run_command(command45)

    command46 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat" -n "fast camera, fast animation, bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  " -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 6 '
    run_command(command46)

    command47 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 7 '
    run_command(command47)

    command48 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 8 '
    run_command(command48)

    command49 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 9 '
    run_command(command49)

    command50 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 10 '
    run_command(command50)
    
    command51 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a gun, close up" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 11 '
    run_command(command51)

    command52 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a gun, wide shot" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 12 '
    run_command(command52)

    command53 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a gun, close up" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 13 '
    run_command(command53)

    command54 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 14 '
    run_command(command54)

    command55 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 15 '
    run_command(command55)

    command56 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 16 '
    run_command(command56)

    command57 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping"  -T 24  -s 3 -pfx 17 '
    run_command(command57)  

    command58 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 18 '
    run_command(command58)

    command59 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 19 '
    run_command(command59)

    command60 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 20 '
    run_command(command60)

    command61 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 21 '
    run_command(command61)

    command62 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 22 '
    run_command(command62)

    command63 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"  -T 24  -s 3  -pfx 23 '
    run_command(command63)

    command64 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"  -T 24  -s 3  -pfx 24 '
    run_command(command64)

    command65 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"  -T 24  -s 3  -pfx 25 '
    run_command(command65)

    command66 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"   -T 24  -s 3  -pfx 26 '
    run_command(command66)

    command67 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"   -T 24  -s 3  -pfx 27 '
    run_command(command67)

    command68 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"   -T 24  -s 3  -pfx 28 '
    run_command(command68)

    command69 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"   -T 24  -s 3  -pfx 29 '
    run_command(command69)

    command70 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 30 '
    run_command(command70)
    
    command71 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 31 '
    run_command(command71)

    command72 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command72)


    command73 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command73)

    command74 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command74)

    command75 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 35 '
    run_command(command75)

    command76 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command76)

    command77 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command77)

    command78 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command78)

    command79 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command79)

    command80 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 40 '
    run_command(command80)

    command81 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 41 '
    run_command(command81)

    command82 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n man in a hat, close up on the face" -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 2  '
    run_command(command82)

    command83 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 3 '
    run_command(command83)

    command84 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 4 '
    run_command(command84)

    command85 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 5 '
    run_command(command85)

    command86 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat" -n "fast camera, fast animation, bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  " -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 6 '
    run_command(command86)

    command87 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 7 '
    run_command(command87)

    command88 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 8 '
    run_command(command88)

    command89 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 9 '
    run_command(command89)

    command90 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 10 '
    run_command(command90)
    
    command91 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a gun, close up" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 11 '
    run_command(command91)

    command92 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a gun, wide shot" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 12 '
    run_command(command92)

    command93 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a gun, close up" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 13 '
    run_command(command93)

    command94 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 14 '
    run_command(command94)

    command95 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 15 '
    run_command(command95)

    command96 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 16 '
    run_command(command96)

    command97 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping"  -T 24  -s 3 -pfx 17 '
    run_command(command97)  

    command98 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 18 '
    run_command(command98)

    command99 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 19 '
    run_command(command99)

    command100 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 20 '
    run_command(command100)

    command101 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 1  '
    run_command(command101)

    command102 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n man in a hat, close up on the face" -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 2  '
    run_command(command102)

    command103 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 3 '
    run_command(command103)

    command104 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 4 '
    run_command(command104)

    command105 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 5 '
    run_command(command105)

    command106 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat" -n "fast camera, fast animation, bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  " -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 6 '
    run_command(command106)

    command107 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 7 '
    run_command(command107)

    command108 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 8 '
    run_command(command108)

    command109 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 9 '
    run_command(command109)

    command110 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 10 '
    run_command(command110)
    
    command111 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a gun, close up" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 11 '
    run_command(command111)

    command112 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a gun, wide shot" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 12 '
    run_command(command112)

    command113 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a gun, close up" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 13 '
    run_command(command113)

    command114 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 14 '
    run_command(command114)

    command115 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 15 '
    run_command(command115)

    command116 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 16 '
    run_command(command116)

    command117 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping"  -T 24  -s 3 -pfx 17 '
    run_command(command117)  

    command118 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 18 '
    run_command(command118)

    command119 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 19 '
    run_command(command119)

    command120 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 20 '
    run_command(command120)

    command121 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 21 '
    run_command(command121)

    command122 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 22 '
    run_command(command122)

    command123 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"  -T 24  -s 3  -pfx 23 '
    run_command(command123)

    command124 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"  -T 24  -s 3  -pfx 24 '
    run_command(command124)

    command125 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"  -T 24  -s 3  -pfx 25 '
    run_command(command125)

    command126 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"   -T 24  -s 3  -pfx 26 '
    run_command(command126)

    command127 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"   -T 24  -s 3  -pfx 27 '
    run_command(command127)

    command128 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"   -T 24  -s 3  -pfx 28 '
    run_command(command128)

    command129 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"   -T 24  -s 3  -pfx 29 '
    run_command(command129)

    command130 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 30 '
    run_command(command130)
    
    command131 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 31 '
    run_command(command131)

    command132 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command132)


    command133 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command133)

    command134 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command134)

    command135 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 35 '
    run_command(command135)

    command136 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command136)

    command137 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command137)

    command138 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command138)

    command139 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command139)

    command140 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 40 '
    run_command(command140)

    command141 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 41 '
    run_command(command141)

    command142 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n man in a hat, close up on the face" -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 2  '
    run_command(command142)

    command143 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 3 '
    run_command(command143)

    command144 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 4 '
    run_command(command144)

    command145 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 5 '
    run_command(command145)

    command146 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat" -n "fast camera, fast animation, bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  " -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 6 '
    run_command(command146)

    command147 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 7 '
    run_command(command147)

    command148 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 8 '
    run_command(command148)

    command149 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 9 '
    run_command(command149)

    command150 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 10 '
    run_command(command150)
    
    command151 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a gun, close up" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 11 '
    run_command(command151)

    command152 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a gun, wide shot" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 12 '
    run_command(command152)

    command153 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a gun, close up" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 13 '
    run_command(command153)

    command154 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 14 '
    run_command(command154)

    command155 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 15 '
    run_command(command155)

    command156 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 16 '
    run_command(command156)

    command157 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping"  -T 24  -s 3 -pfx 17 '
    run_command(command157)  

    command158 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 18 '
    run_command(command158)

    command59 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 19 '
    run_command(command159)

    command160 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 20 '
    run_command(command160)

    command161 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 21 '
    run_command(command161)

    command162 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 22 '
    run_command(command62)

    command163 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"  -T 24  -s 3  -pfx 23 '
    run_command(command163)

    command164 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"  -T 24  -s 3  -pfx 24 '
    run_command(command164)

    command165 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"  -T 24  -s 3  -pfx 25 '
    run_command(command165)

    command166 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"   -T 24  -s 3  -pfx 26 '
    run_command(command166)

    command167 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"   -T 24  -s 3  -pfx 27 '
    run_command(command167)

    command168 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"   -T 24  -s 3  -pfx 28 '
    run_command(command168)

    command169 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast movement", "bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  , fast animation, fast characters, fast camera, running , jumping"   -T 24  -s 3  -pfx 29 '
    run_command(command169)

    command170 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 30 '
    run_command(command170)
    
    command171 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 31 '
    run_command(command171)

    command172 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command172)


    command173 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command173)

    command174 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command174)

    command175 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 35 '
    run_command(command175)

    command176 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command176)

    command177 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command177)

    command178 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command178)

    command179 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 34 '
    run_command(command179)

    command180 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 40 '
    run_command(command180)

    command181 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat, camera pan left" -n "fast camera movement, fast animation, fast character movement, running , jumping"  -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 41 '
    run_command(command181)

    command182 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n man in a hat, close up on the face" -T 24  -s 3 --width 576 --height 384 -f 6   -pfx 2  '
    run_command(command182)

    command183 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 3 '
    run_command(command183)

    command184 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 4 '
    run_command(command184)

    command185 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 5 '
    run_command(command185)

    command186 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat staring at another man with a hat" -n "fast camera, fast animation, bad anatomy, bad hands, three hands, three legs, bad arms, missing legs,  " -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 6 '
    run_command(command186)

    command187 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 7 '
    run_command(command187)

    command188 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 8 '
    run_command(command188)

    command189 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 9 '
    run_command(command189)

    command190 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement" -T 24  -s 3 --width 576 --height 384 -f 6  -pfx 10 '
    run_command(command190)
    
    command191 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a gun, close up" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 11 '
    run_command(command191)

    command192 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a gun, wide shot" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 12 '
    run_command(command192)

    command193 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a gun, close up" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 13 '
    run_command(command193)

    command194 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 14 '
    run_command(command194)

    command195 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 15 '
    run_command(command195)

    command196 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 16 '
    run_command(command196)

    command197 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping"  -T 24  -s 3 -pfx 17 '
    run_command(command197)  

    command198 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 18 '
    run_command(command198)

    command199 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p man in a hat, close up on the face" -n "fast camera movement, running , fast animation, fast characters, fast camera, running , jumping" -T 24  -s 3 -pfx 19 '
    run_command(command199)

    command200 = 'python inference.py --model /Text-To-Video-Finetuning/zeroscope_v2_576w/ -p "a man with a hat shooting a rifle in the desert" -n "fast camera movement, fast animation, fast character movement, running , jumping" -T 24  -s 3  -pfx 20 '
    run_command(command200)
  
if __name__ == "__main__":
    main()


