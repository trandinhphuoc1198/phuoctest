import requests,m3u8,subprocess
#First find m3u8 file
#Then choose a resolution in 'playlists' of that m3u8 file data
#Finally, download the videos from list in 'uri'
m3u8file=requests.get('https://znews-mcloud-lpl-s2-te-vnno-zn-8.zingcdn.me/nWcMKk9Tok8/whls/vod/1080/MrTMsDMT30a92GcfKTm/f89ecda029c4c09a99d5.m3u8?authen=exp=1652953077~acl=/nWcMKk9Tok8/*~hmac=773c2c932e5694f1436f97ca3db765e3')
m3u8_master=m3u8.loads(m3u8file.text)

host='https:'
with open('zingvideo.ts','wb') as f:
    for i in m3u8_master.data['segments']:
        r=requests.get(host+i['uri'])
        f.write(r.content)

subprocess.run('ffmpeg -i zingvideo.ts vid1.mp4',shell=True)
