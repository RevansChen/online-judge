# Python3

from solution1 import frequencyAnalysis as f

qa = [
    ('$~NmiNmim$/NVeirp@dlzrCCCCfFfQQQ',
     'C'),
    ("Agoodglassinthebishop'shostelinthedevil'sseattwenty-onedegreesandthirteenminutesnortheastandbynorthmainbranchseventhlimbeastsideshootfromthelefteyeofthedeath's-headabeelinefromthetreethroughtheshotfiftyfeetout.",
     'e'),
    ('Q',
     'Q'),
    ('):<<}:BnUUKc=>~LKU><,;U><U=~BKc=>~}~jKB;UU~n== ~c=fS<c~}~:w~~Unc}=>Kw=~~ceKc*=~Uc<w=>~nU=nc}Lfc<w=>enKcLwncY>U~j~c=>BKeL~nU=UK}~U><<=mw<e=>~B~m=~f~<m=>~}~n=>;US>~n}nL~~BKc~mw<e=>~=w~~=>w<*:>=>~U><=mKm=fm~~=<*=k',
     '~'),
    ("(:c:@%aF;:NBo@o:'X:%CFCBoFB@X@iFCTPc@iFi::@o%;@a!PXCF:iTcCNbCFPoFCc;:YCo%a@a}Pcco@Cc:%@FF;::o%BYBo:bi@oT;=nFv:|i@o%`a%Ci:TFCBo<!PXCF:i%iBXaF;:bP|F;iBP|;Bo:: :aBT}:F@o%v:|i@o%X@T:aBPFFB@aXBF*;:i:F;:|iBPXb:|CoaFB%C|=$Co%Co|oBF;Co|F;:i:<v:|i@o%;@a!PXCF:iTcCNbF;:Fi::@|@Co@o%%iBXF;:bP|F;iBP|;F;:a}Pcc`aBF;:i: :dF;: T;BBa:@%CYY:i:oFaXBFFB%C|<F;CaFCN:YCo%Co|F*Ba}:c:FBoa@o%@T;:aFYCcc:%*CF;|Bc%TBCoa@o%D:*:ci =V;: :aFCN@F:F;:FBF@cE@cP:@Fj1=5NCccCBo<bPF:E:oF;@FYC|Pi:XiBE:aFBb:b:cB*F;:@TFP@c*BiF;*;:oF;: :E:oFP@cc a:ccF;:CF:Na=",
     ':')
]

for *q, a in qa:
    for i, e in enumerate(q):
        print('input{0}: {1}'.format(i + 1, e))
    ans = f(*q)
    if ans != a:
        print('  [failed]')
        print('    output:', ans)
        print('    expected:', a)
    else:
        print('  [ok]')
        print('    output:', ans)
    print()
