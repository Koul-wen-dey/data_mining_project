def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return C1

def scanD(D,Ck,minSupport):
    # ssCnt 臨時存放所有候選項集和頻率.
    ssCnt = {}
    for tid in D:
        for can in map(frozenset,Ck):      #每個候選項集can
            # print('2:',can.issubset(tid),can,tid)
            if can.issubset(tid):
                if not can in ssCnt:
                    ssCnt[can] = 1
                else:
                    ssCnt[can] +=1

    numItems = float(len(D)) # 所有項集數目
    # 滿足最小支援度的頻繁項集
    retList  = []
    # 滿足最小支援度的頻繁項集和頻率
    supportData = {}

    for key in ssCnt:
        support = ssCnt[key]/numItems   #除以總的記錄條數，即為其支援度
        if support >= minSupport:
            retList.insert(0,key)       #超過最小支援度的項集，將其記錄下來。
        supportData[key] = support
    return retList, supportData

def aprioriGen(Lk, k):
    retList = [] # 滿足條件的頻繁項集
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk):
            L1 = list(Lk[i])[: k-2]
            L2 = list(Lk[j])[: k-2]
            # print '-----i=', i, k-2, Lk, Lk[i], list(Lk[i])[: k-2]
            # print '-----j=', j, k-2, Lk, Lk[j], list(Lk[j])[: k-2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList

def apriori(dataSet, minSupport=0.5):
    # C1即對dataSet去重排序，然後轉換所有的元素為frozenset
    C1 = createC1(dataSet)
    # 對每一行進行 set 轉換，然後存放到集合中
    D = list(map(set, dataSet))
    # 計算候選資料集C1在資料集D中的支援度，並返回支援度大於minSupport 的資料
    L1, supportData = scanD(D, C1, minSupport)
    # L 加了一層 list, L一共 2 層 list
    L = [L1];k = 2
    # 判斷L第k-2項的資料長度是否>0即頻繁項集第一項。第一次執行時 L 為 [[frozenset([1]), frozenset([3]), frozenset([2]), frozenset([5])]]。L[k-2]=L[0]=[frozenset([1]), frozenset([3]), frozenset([2]), frozenset([5])]，最後面 k += 1
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k) # 例如: 以 {0},{1},{2} 為輸入且 k = 2 則輸出 {0,1}, {0,2}, {1,2}. 以 {0,1},{0,2},{1,2} 為輸入且 k = 3 則輸出 {0,1,2}

        # 返回候選資料集CK在資料集D中的支援度大於最小支援度的資料
        Lk, supK = scanD(D, Ck, minSupport)
        # 儲存所有候選項集的支援度，如果字典沒有就追加元素，如果有就更新元素
        supportData.update(supK)
        if len(Lk) == 0:
            break
        # Lk 表示滿足頻繁子項的集合，L 元素在增加，例如:
        # l=[[set(1), set(2), set(3)]]
        # l=[[set(1), set(2), set(3)], [set(1, 2), set(2, 3)]]
        L.append(Lk)
        k += 1
        print(len(D))
    return L, supportData

def testApriori():
    # 載入測試資料集
    dataSet = loadDataSet()
    print ('dataSet: ', dataSet)

    # Apriori 演算法生成頻繁項集以及它們的支援度
    L1, supportData1 = apriori(dataSet, minSupport=0.7)
    # print ('L(0.7): ', L1)
    # print ('supportData(0.7): ', supportData1)

def calcConf(freqSet, H, supportData, brl, minConf=0.7):
    # 記錄可信度大於最小可信度（minConf）的集合
    prunedH = []
    for conseq in H: # 假設 freqSet = frozenset([1, 3]), H = [frozenset([1]), frozenset([3])]，那麼現在需要求出 frozenset([1]) -> frozenset([3]) 的可信度和 frozenset([3]) -> frozenset([1]) 的可信度
        conf = supportData[freqSet]/supportData[freqSet-conseq] # 支援度定義: a -> b = support(a | b) / support(a). 假設  freqSet = frozenset([1, 3]), conseq = [frozenset([1])]，那麼 frozenset([1]) 至 frozenset([3]) 的可信度為 = support(a | b) / support(a) = supportData[freqSet]/supportData[freqSet-conseq] = supportData[frozenset([1, 3])] / supportData[frozenset([1])]
        if conf >= minConf:
            # 只要買了 freqSet-conseq 集合，一定會買 conseq 集合（freqSet-conseq 集合和 conseq集合 是全集）
            print (freqSet-conseq, '-->', conseq, 'conf:', conf)
            brl.append((freqSet-conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH

def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    # H[0] 是 freqSet 的元素組合的第一個元素，並且 H 中所有元素的長度都一樣，長度由 aprioriGen(H, m+1) 這裡的 m + 1 來控制
    # 該函式遞迴時，H[0] 的長度從 1 開始增長 1 2 3 ...
    # 假設 freqSet = frozenset([2, 3, 5]), H = [frozenset([2]), frozenset([3]), frozenset([5])]
    # 那麼 m = len(H[0]) 的遞迴的值依次為 1 2
    # 在 m = 2 時, 跳出該遞迴。假設再遞迴一次，那麼 H[0] = frozenset([2, 3, 5])，freqSet = frozenset([2, 3, 5]) ，沒必要再計算 freqSet 與 H[0] 的關聯規則了。
    m = len(H[0])
    if (len(freqSet) > (m + 1)):
        # 生成 m+1 個長度的所有可能的 H 中的組合，假設 H = [frozenset([2]), frozenset([3]), frozenset([5])]
        # 第一次遞迴呼叫時生成 [frozenset([2, 3]), frozenset([2, 5]), frozenset([3, 5])]
        # 第二次 。。。沒有第二次，遞迴條件判斷時已經退出了
        Hmp1 = aprioriGen(H, m+1)
        # 返回可信度大於最小可信度的集合
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
        # print ('Hmp1=', Hmp1)
        # print ('len(Hmp1)=', len(Hmp1), 'len(freqSet)=', len(freqSet))
        # 計算可信度後，還有資料大於最小可信度的話，那麼繼續遞迴呼叫，否則跳出遞迴
        if (len(Hmp1) > 1):
            # print '----------------------', Hmp1
            # print len(freqSet),  len(Hmp1[0]) + 1
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)

def generateRules(L, supportData, minConf=0.7):
    bigRuleList = []
    for i in range(1, len(L)):
        # 獲取頻繁項集中每個組合的所有元素
        for freqSet in L[i]:
            # 組合總的元素並遍歷子元素，轉化為 frozenset集合存放到 list 列表中
            H1 = [frozenset([item]) for item in freqSet]
            # print(H1)
            # 2 個的組合else, 2 個以上的組合 if
            if (i > 1):
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList

def testGenerateRules():
    # 載入測試資料集
    dataSet = loadDataSet()
    # print ('dataSet: ', dataSet)
    print('')
    # Apriori 演算法生成頻繁項集以及它們的支援度
    L1, supportData1 = apriori(dataSet, minSupport=0.5)
    # print ('L(0.7): ', L1)
    # print ('supportData(0.7): ', supportData1)

    # 生成關聯規則
    rules = generateRules(L1, supportData1, minConf=0.5)
    for r in rules:
        print(r)

if '__main__' == __name__:
    minSupport = 0.5
    dataSet = loadDataSet()
    testApriori()
