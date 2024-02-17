
import gmpy2
import  binascii
from Crypto.Util.number import *
from gmpy2 import *

## sage LLL 算法解出 d
"""
PB=[(72752611476377764174764112463276565833319383318569424425229281693729423644687510505134144629941459787532264555742574465246465193035126330171199507442838642461689118156329994912696356451046021921283404110079064080241687715837798377772669637888103687968138613253784192033783530917951876095979512525540038659899, 21976930964659045345752324191113315596319970094523677115144003715054090103791440991420482895285491266869247953713992105387268594509561200647508049224051888545750812831120610156603030407925724811054612881294926623732679266572828561532710945312628578841722550877648726793324617926503665023048901391056184318029),
(129178306526123899098107425198898104780679643650849320297569495024718538163658658913330766505270357612361983235541332319689809600479672164816160663354821282291039659655555937959740586836162501422419797207250176681475267167328274012174818517018665858833463954458600047386358013307824968313043206859142040900153, 31089243881339881401139133462881313585962854331314376941603933360076794678352113561751929675463968799551217117623208464847715353696161837886528465639286311936723730506139145096365483505175939836146968858556553906907796418719327572687542115567318457128625169147316648696834407712098622201933446179891290046851),
(145629652279838968628833534988426878286462745747919991141140041593027588505496310715726797411360984728895873951618183484295413633797384880640205169022452680419940786177840685409487666103930718538713184118039353302236502828236328781311589502694610098213508742013289892743156231783366952225959946457483255538171, 108518082648321969317421532945465270670230129786595206715223244540390457530206948822118686175838666206134326577075882026977258586062617946844590333588083057035671717081091144619446377746524265495107711467508362177994941048846502677302433939939620296545690138363515253572466039910887397359471721466866442786961)]
C=[26110208124071369292261841473391627640997994594855717612104942523064770539429045387666757318941812508405986506504762252835721708197282577156228849075171281126017243508178458486756735681882907553628344893382560756335664142564034339854029763571503891060054720705857369564337829424937179991039284489691681452799, 44267254782173769940160070878465586057201073658697129441180622476069606393421894158759108204110263220880479089959267863983279987809115166311906897361774652919511937479126138773595668881437662000900837551814521463765744567524835330466921970347324344579861469353624720934046170676482430979090686265958374746895, 144479981402309358993876163829320503018212926776017346569537171716042249252416461175410220805542157669225844953419024310595493784453514225564227763392722832076265337747280825938223391757089109302643400745108582831634581061685443095025386138122921789500127336286518127557369481517373927271742743675091444547732]

e0 = PB[0][1]
n0 = PB[0][0]
e1 = PB[1][1]
n1 = PB[1][0]
e2 = PB[2][1]
n2 = PB[2][0]
c0 = C[0]
c1 = C[1]
c2 = C[2]

M1 = Matrix(4,4,0)
temp = int(n1)
M = isqrt(max(n0,n1,n2))
M1[0,0] = M
M1[0,1] = e0
M1[0,2] = e1
M1[0,3] = e2
M1[1,1] = -n0
M1[2,2] = -n1
M1[3,3] = -n2
BL = M1.LLL()
# print (BL)
v = M1.solve_left(BL[0])
k1 = v[1]
d = abs(BL[0,0])/M
print(d)
ed = BL[0,1] + k1 * n0
print(ed % d)
"""

d = 58231633848553043790269852976140494812403119460045849603007921960688440364797340250675586701

# e = 108518082648321969317421532945465270670230129786595206715223244540390457530206948822118686175838666206134326577075882026977258586062617946844590333588083057035671717081091144619446377746524265495107711467508362177994941048846502677302433939939620296545690138363515253572466039910887397359471721466866442786961
# n = 145629652279838968628833534988426878286462745747919991141140041593027588505496310715726797411360984728895873951618183484295413633797384880640205169022452680419940786177840685409487666103930718538713184118039353302236502828236328781311589502694610098213508742013289892743156231783366952225959946457483255538171
# c = 144479981402309358993876163829320503018212926776017346569537171716042249252416461175410220805542157669225844953419024310595493784453514225564227763392722832076265337747280825938223391757089109302643400745108582831634581061685443095025386138122921789500127336286518127557369481517373927271742743675091444547732

n = 72752611476377764174764112463276565833319383318569424425229281693729423644687510505134144629941459787532264555742574465246465193035126330171199507442838642461689118156329994912696356451046021921283404110079064080241687715837798377772669637888103687968138613253784192033783530917951876095979512525540038659899
e = 21976930964659045345752324191113315596319970094523677115144003715054090103791440991420482895285491266869247953713992105387268594509561200647508049224051888545750812831120610156603030407925724811054612881294926623732679266572828561532710945312628578841722550877648726793324617926503665023048901391056184318029
c = 26110208124071369292261841473391627640997994594855717612104942523064770539429045387666757318941812508405986506504762252835721708197282577156228849075171281126017243508178458486756735681882907553628344893382560756335664142564034339854029763571503891060054720705857369564337829424937179991039284489691681452799
## bit数需满足  (ed-1)*f(p,q)<n^2 ，本题 (ed-1)*f(p,q) = 1024+305+512=1841 n^2=2048
## ed-1 = k(N +2(p+q) + 4) = kN + k(2p+2q+4) (0< k(2p+2q+4)/N <1)  所以计算 k = ed-1 // N;   
## 如果 -1 < PhiN - N < 0 需要计算 k = ed-1 // N; k=k+1;
## phi = (ed-1) / k
k  = (e*d -1) //n
print(k)
phiN = (e*d -1) // k
print(phiN)
## fake_phi = (p+2)(q+2) 
## p+q = (fake_phi -N -4)/2
P_Q = (phiN - n -4) //2 
print(P_Q)
PhiN = phiN -3* P_Q-3

rd = inverse(e,PhiN)

print(long_to_bytes(powmod(c,rd,n)))

## 分解 p q
p = abs((-P_Q + gmpy2.iroot(P_Q**2-4*n, 2)[0])//2)
q = n // p
print(p,q)


"""
from gmpy2 import *
from Crypto.Util.number import *
pubkeys =
[(727526114763777641747641124632765658333193833185694244252292816937294236446875
10505134144629941459787532264555742574465246465193035126330171199507442838642461
68911815632999491269635645104602192128340411007906408024168771583779837777266963
7888103687968138613253784192033783530917951876095979512525540038659899,
21976930964659045345752324191113315596319970094523677115144003715054090103791440
99142048289528549126686924795371399210538726859450956120064750804922405188854575
08128311206101566030304079257248110546128812949266237326792665728285615327109453
12628578841722550877648726793324617926503665023048901391056184318029),
(1291783065261238990981074251988981047806796436508493202975694950247185381636586
58913330766505270357612361983235541332319689809600479672164816160663354821282291
03965965555593795974058683616250142241979720725017668147526716732827401217481851
7018665858833463954458600047386358013307824968313043206859142040900153,
31089243881339881401139133462881313585962854331314376941603933360076794678352113
56175192967546396879955121711762320846484771535369616183788652846563928631193672
37305061391450963654835051759398361469688585565539069077964187193275726875421155
67318457128625169147316648696834407712098622201933446179891290046851),
(1456296522798389686288335349884268782864627457479199911411400415930275885054963
10715726797411360984728895873951618183484295413633797384880640205169022452680419
94078617784068540948766610393071853871318411803935330223650282823632878131158950
2694610098213508742013289892743156231783366952225959946457483255538171,
10851808264832196931742153294546527067023012978659520671522324454039045753020694
88221186861758386662061343265770758820269772585860626179468445903335880830570356
71717081091144619446377746524265495107711467508362177994941048846502677302433939
939620296545690138363515253572466039910887397359471721466866442786961)]
cs =
[2611020812407136929226184147339162764099799459485571761210494252306477053942904
53876667573189418125084059865065047622528357217081972825771562288490751712811260
17243508178458486756735681882907553628344893382560756335664142564034339854029763
571503891060054720705857369564337829424937179991039284489691681452799,
44267254782173769940160070878465586057201073658697129441180622476069606393421894
15875910820411026322088047908995926786398327998780911516631190689736177465291951
19374791261387735956688814376620009008375518145214637657445675248353304669219703
47324344579861469353624720934046170676482430979090686265958374746895,
14447998140230935899387616382932050301821292677601734656953717171604224925241646
11754102208055421576692258449534190243105954937844535142255642277633927228320762
65337747280825938223391757089109302643400745108582831634581061685443095025386138
122921789500127336286518127557369481517373927271742743675091444547732]
n1,e1,n2,e2,n3,e3 = pubkeys[0][0],pubkeys[0][1],pubkeys[1][0],pubkeys[1]
[1],pubkeys[2][0],pubkeys[2][1]
assert n1 < n2 < n3
M=iroot(int(n3),int(2))[0]
a=[0]*4
a[0]=[M,e1,e2,e3]
a[1]=[0,-n1,0,0]
a[2]=[0,0,-n2,0]
a[3]=[0,0,0,-n3]
Mat = matrix(ZZ,a)
Mat_LLL=Mat.LLL()[0]
t1 = Mat_LLL[1]
# 求系数k1，k2
v = Mat.solve_left(Mat_LLL)
k1 = v[1]
s1 = (1 - t1)//k1
p1plusq1 = (-s1 - 4) // 2
print(p1plusq1)
p, q = var('p, q')
solve([p + q == p1plusq1,p * q == n1], p, q)
p =
67075295228620750016704014476957711881767563712789063102655276176680354864772900
56801973207466400059834517477939564970648196493934829504401197938124556161
q =
10846409431133525131922903636399026239432250344765616101182078802246191172322863
128313905167909804719567705837705547296565292750722911818943402614161462459
phi = (p-1)*(q-1)
d = inverse_mod(e1,phi)
c1 = cs[0]
print(long_to_bytes(ZZ(pow(c1,d,n1))))
"""