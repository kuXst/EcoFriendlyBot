import discord

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} OLARAK SUNUCUYA DALDI.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.çevre'):
        await message.channel.send("Çevreyi korumak için yapmamız gerekenler oldukkça basittir. Plastik kullanımı azaltmak, çevreye çöp atmakak bunlardan bazılarıdır  ")
    elif message.content.startswith('.çdu'):
        await message.channel.send("Çevre dostu uygulamalar çevre katkı sağlamak amaçlı oluşturulmuş uygulamalardır. Bunlardan bazıları: Forest, Earth Hero, JouleBug, Ecosia  ")
    elif message.content.startswith(".forest"):
        await message.channel.send("iOS ve Android uyumlu Forest, siz çalışırken ekranda adeta bir sanal ağaç büyütüyor. Böylece sizi daha üretken olmaya teşvik ediyor. Uygulamayı kullanabilmek için ise tek yapmanız gereken, ne kadar süre odaklanmak istediğinizi seçmek. Sonrasında geri sayım sayacı, süre dolana kadar bildirimlerinizi sessize alarak ekranınızda ağaç büyütmeye başlıyor.  ")    
    elif message.content.startswith('.EH'):
        await message.channel.send("Çevreci uygulamalar arasında öne çıkan Earth Hero, iklim krizi üzerinde etkiye sahip olmanıza imkan tanıyor. Karbon kirliliğini azaltmaya yönelik kişisel eylemlerinizin yanı sıra diğer insanların da çevreyi kirleten alışkanlıklarını değiştirmelerine yardımcı olmanızı sağlıyor. ")
    elif message.content.startswith('.JB'):
        await message.channel.send("Çevre dostu uygulamalar kapsamında kullanıcılardan tam not alan bir yazılım da JouleBug. Sürdürülebilirliği oyuna dönüştüren bu uygulama, gerçekleştirmiş olduğunuz her çevreci hareket için size puan kazandırıyor. Son derece basit görevlerle başlayan JouleBug, daha sonra zorlaşarak devam ediyor.  ")
    elif message.content.startswith('.ecosia'):
        await message.channel.send("Yapılan her 45 arama ile bir ağaç dikilmesini sağlayan Ecosia sayesinde günümüzde 104 milyon 500 bin ağaç dikilmiş durumda. Sunucuları yüzde yüz yenilenebilir enerji ile çalışan uygulamada her arama talebi atmosferden 1 kg CO2 yok ediyor.  ")
    elif message.content.startswith('.help'):
        await message.channel.send(".çevre , .çdu , .forest , .EH , .Jb , .ecosia  ")




client.run("TOKEN TOKEN TOKEN")
