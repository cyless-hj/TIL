def replace(m):
    for a,b in zip(["A#", "C#", "D#", "F#", "G#"], ["T","U","I","O","P"]):
        m = m.replace(a,b)
    return m

def solution(m, musicinfos):
    answer = ''
    m = replace(m)
    arr = []
    for info in musicinfos:
        music = list(info.split(','))
        print(music)
        runtime = (int(music[1].split(":")[0]) - int(music[0].split(":")[0])) * 60 + int(music[1].split(":")[1]) - int(music[0].split(":")[1])
        music[3] = replace(music[3])
        q, r = divmod(runtime, len(music[3]))
        music[3] = music[3] * q + music[3][:r]
        if m in music[3]:
            arr.append(music)
    arr.sort(key= lambda x:-len(x[3]))
    if arr:
        answer = arr[0][2]
    else:
        answer = '(None)'
    return answer