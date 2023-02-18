from collections import deque # python da queue tuzilmasi bilan ishlash uchun modul

def search(starn_node,target="doctor"):#qayerdan boshlash va kimni qidirayotganimizni kiritamiz
    search_queue = deque()#izlayotgan royxatimizni queue korinishida yaratyabmiz
    search_queue += graph[starn_node]#izlayotkan odamning aloqalarini royzatga qoshyabmiz
    searched = set()#qayta izlashga vaqt sariflamaslik uchun noyob list yaratib olyabmiz

    while search_queue:#izlash sikli, shartimiz toki queue da odam tugamaguncha
        person = search_queue.popleft()#queue dan birinchi odamni qarayabmiz va queuedan ochiryabmiz
        if person==target:#tekshiryabmiz
            print(f'{target}ni topdik!')
            print(searched)
            return True
        else:#aks holda
            search_queue += graph[person]#hozirgi odamni aloqalarini queue ga qoshyabmiz
            searched.add(person)#izlab bolganlar qotoriga qoshyabmiz
    return False#agar topa olmasak False qaytartabmiz

if __name__ == '__main__':
    graph = {'siz':['ali','vali','tohir'],'ali':['aziza','olim'],'vali':['botir','ziyoda'],
             'tohir':['doctor','mohir'], 'olim':[],'aziza': [], 'botir':[], 'ziyoda':['aziza'],'doctor':[],'mohir':[]}
    print(search('siz',"doctor"))