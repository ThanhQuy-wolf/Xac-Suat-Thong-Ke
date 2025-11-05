# Ex1: A box contains three marbles — one red, one green, and one blue. Consider an experiment that consists of taking one marble from the box, then replacing it in the box and drawing a second marble from the box. Describe the sample space. Repeat for the case in which the second marble is drawn without first replacing the first marble.
## Dịch sang tiếng Việt
Một hộp chứa ba viên bi — một viên đỏ, một viên xanh lá cây và một viên xanh dương. Xem xét một thí nghiệm bao gồm việc lấy một viên bi từ hộp, sau đó đặt nó trở lại hộp và rút viên bi thứ hai từ hộp. Mô tả không gian mẫu. Lặp lại cho trường hợp rút viên bi thứ hai mà không đặt viên bi đầu tiên trở lại hộp.
## Giải
- Lần đầu tiên, ta có thể rút một trong ba viên bi: Đỏ (R), Xanh lá cây (G), hoặc Xanh dương (B). Là tổ hợp {R, G, B} = 3.
- Sau khi rút viên bi đầu tiên, ta đặt nó trở lại hộp. Do đó, lần thứ hai ta vẫn có thể rút một trong ba viên bi. Là tổ hợp {R, G, B} = 3.
- Tổng = tích của số kết quả của lần rút đầu tiên và số kết quả của lần rút thứ hai: 3 * 3 = 9.
- Không gian mẫu (S) bao gồm tất cả các tổ hợp có thể xảy ra khi rút hai viên bi:
  S = { (R, R), (R, G), (R, B), (G, R), (G, G), (G, B), (B, R), (B, G), (B, B) }
- Nếu sau khi rút viên bi đầu tiên, ta không đặt nó trở lại hộp, thì lần thứ hai ta chỉ có thể rút một trong hai viên bi còn lại.
- Tổng = tích của số kết quả của lần rút đầu tiên và số kết quả của lần rút thứ hai: 3 * 2 = 6.
- Không gian mẫu (S) bao gồm tất cả các tổ hợp có thể xảy ra khi rút hai viên bi mà không đặt viên bi đầu tiên trở lại hộp:
  S = { (R, G), (R, B), (G, R), (G, B), (B, R), (B, G) }

# Ex2: An experiment consists of tossing a coin three times. What is the sample space of this experiment? Which event corresponds to the experiment resulting in more heads than tails?
## Dịch sang tiếng Việt
Một thí nghiệm bao gồm việc tung một đồng xu ba lần. Không gian mẫu của thí nghiệm này là gì? Sự kiện nào tương ứng với việc thí nghiệm có nhiều mặt ngửa hơn mặt sấp?
## Giải
- Không gian mẫu (S) của thí nghiệm này bao gồm tất cả các kết quả có thể xảy ra khi tung đồng xu ba lần:
  S = { (H, H, H), (H, H, T), (H, T, H), (H, T, T), (T, H, H), (T, H, T), (T, T, H), (T, T, T) }
- Trong đó H đại diện cho mặt ngửa và T đại diện cho mặt sấp.
- Sự kiện có nhiều mặt ngửa hơn mặt sấp có thể được mô tả như sau:
  E = { (H, H, H), (H, H, T), (H, T, H), (T, H, H) }
- Vậy sự kiện E bao gồm các kết quả có ít nhất hai mặt ngửa.

# Ex3: Let S = { 1, 2, 3, 4, 5, 6, 7 } , E = { 1, 3, 5, 7 } , F = { 7, 4, 6 } , G = { 1, 4 } . Find (a) EF ; (c) EG c ; (e) E c ( F ∪ G ) ; (b) E ∪ FG ; (d) EF c ∪ G ; (f ) EG ∪ FG
## Câu a
- EF = E ∩ F = { 1, 3, 5, 7 } ∩ { 7, 4, 6 } = { 7 }
## Câu b
- E ∪ FG = E ∪ (F ∩ G) = { 1, 3, 5, 7 } ∪ ({ 7, 4, 6 } ∩ { 1, 4 }) = { 1, 3, 5, 7 } ∪ { 4 } = { 1, 3, 4, 5, 7 }
## Câu c
- EG c = E ∩ G c = { 1, 3, 5, 7 } ∩ { 2, 3, 5, 6, 7 } = { 3, 5, 7 }
## Câu d
- EF c ∪ G = (E ∩ F c) ∪ G = ({ 1, 3, 5, 7 } ∩ { 1, 2, 3, 5 }) ∪ { 1, 4 } = { 1, 3, 5 } ∪ { 1, 4 } = { 1, 3, 4, 5 }
## Câu e
- E c ( F ∪ G ) = { 2, 4, 6 } ∩ ({ 7, 4, 6 } ∪ { 1, 4 }) = { 2, 4, 6 } ∩ { 1, 4, 6, 7 } = { 4, 6 }
## Câu f
- EG ∪ FG = (E ∩ G) ∪ (F ∩ G) = ({ 1, 3, 5, 7 } ∩ { 1, 4 }) ∪ ({ 7, 4, 6 } ∩ { 1, 4 }) = { 1 } ∪ { } = { 1 }

# Ex4: Two dice are thrown. Let E be the event that the sum of the dice is odd, let F be the event that the first die lands on 1, and let G be the event that the sum is 5. Describe the events EF , E ∪ F , FG , EF c , EFG
## Dich sang tiếng Việt
Hai con xúc xắc được tung. Gọi E là sự kiện tổng của hai con xúc xắc là số lẻ, gọi F là sự kiện con xúc xắc thứ nhất ra mặt 1, và gọi G là sự kiện tổng là 5. Mô tả các sự kiện EF, E ∪ F, FG, EF c, EFG.
## Giải
- Không gian mẫu (S) khi hai con xúc xắc được tung là: 6C1 * 6C1 = 36.
- E là sự kiện tổng của hai con xúc xắc là số lẻ. Điều này xảy ra khi một con xúc xắc ra số chẵn và con còn lại ra số lẻ. => |E| = 18, P(E) = 18/36 = 1/2.
- F là sự kiện con xúc xắc thứ nhất ra mặt 1. => |F| = 6, P(F) = 6/36 = 1/6.
- G là sự kiện tổng là 5. Các cặp (x, y) thỏa mãn x + y = 5 là (1, 4), (2, 3), (3, 2), (4, 1). => |G| = 4, P(G) = 4/36 = 1/9.
- EF là sự kiện tổng của hai con xúc xắc là số lẻ và con xúc xắc thứ nhất ra mặt 1. => EF = {(1,2), (1,4), (1,6)}, |EF| = 3, P(EF) = 3/36 = 1/12.
- E U F là sự kiện tổng của hai con xúc xắc là số lẻ hoặc con xúc xắc thứ nhất ra mặt 1. => E U F = 1/2 + 1/6 - 1/12 = 7/12.
- FG là sự kiện con xúc xắc thứ nhất ra mặt 1 và tổng là 5. => FG = {(1,4)}, |FG| = 1, P(FG) = 1/36.
- EFc là sự kiện tổng của hai con xúc xắc là số lẻ và con xúc xắc thứ nhất không ra mặt 1. => EFc = 18 - 3 = 15, P(EFc) = 15/36 = 5/12.
- EFG là sự kiện tổng của hai con xúc xắc là số lẻ, con xúc xắc thứ nhất ra mặt 1 và tổng là 5. Mà G đã có tổng là 5, nên G là con của E. Do đó EFG = FG = {(1,4)}, |EFG| = 1, P(EFG) = 1/36.

# Ex5: A system is composed of four components, each of which is either working or failed. Consider an experiment that consis ts of observing the status of each component, and let the outcome of the experiment be given by the vector ( x 1 , x 2 , x 3 , x 4 ) where x i is equal to 1 if component i is working and is equal to 0 if component i is failed. (a) How many outcomes are in the sample space of this experiment? (b) Suppose that the system will work if components 1 and 2 are both working, or if components 3 and 4 are both working. Specify all the outcomes in the event that the system works. (c) Let E be the event that components 1 and 3 are bo th failed. How many outcomes are contained in event E ?
## Dịch sang tiếng Việt
Một hệ thống bao gồm bốn thành phần, mỗi thành phần có thể hoạt động hoặc hỏng. Xem xét một thí nghiệm bao gồm việc quan sát trạng thái của mỗi thành phần, và kết quả của thí nghiệm được biểu diễn bằng vector (x1, x2, x3, x4) trong đó xi bằng 1 nếu thành phần i hoạt động và bằng 0 nếu thành phần i hỏng. (a) Có bao nhiêu kết quả trong không gian mẫu của thí nghiệm này? (b) Giả sử hệ thống sẽ hoạt động nếu cả thành phần 1 và 2 đều hoạt động, hoặc nếu cả thành phần 3 và 4 đều hoạt động. Xác định tất cả các kết quả trong sự kiện hệ thống hoạt động. (c) Gọi E là sự kiện thành phần 1 và 3 đều hỏng. Có bao nhiêu kết quả nằm trong sự kiện E?
## Giải
- (a) Mỗi thành phần có 2 trạng thái (hoạt động hoặc hỏng), và có 4 thành phần. Do đó, số kết quả trong không gian mẫu là 2^4 = 16.
- (b) Hệ thống hoạt động nếu:
  - Thành phần 1 và 2 đều hoạt động: (1, 1, x3, x4) với x3 và x4 có thể là 0 hoặc 1. Các kết quả là: (1, 1, 0, 0), (1, 1, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1).
  - Hoặc thành phần 3 và 4 đều hoạt động: (x1, x2, 1, 1) với x1 và x2 có thể là 0 hoặc 1. Các kết quả là: (0, 0, 1, 1), (0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 1, 1).
  - Kết hợp lại, các kết quả trong sự kiện hệ thống hoạt động là: 
    {(1, 1, 0, 0), (1, 1, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1), (0, 0, 1, 1), (0, 1, 1, 1), (1, 0, 1, 1)}.
- (c) Sự kiện E là thành phần 1 và 3 đều hỏng, tức là x1 = 0 và x3 = 0. Các kết quả trong sự kiện E là: (0, x2, 0, x4) với x2 và x4 có thể là 0 hoặc 1. Do đó, số kết quả trong sự kiện E là 2^2 = 4. Các kết quả cụ thể là: (0, 0, 0, 0), (0, 0, 0, 1), (0, 1, 0, 0), (0, 1, 0, 1).

# Ex6:Let E, F, G be three events. Find expressions for the events that of E , F , G (a) only E occurs; (b) both E and G but not F occur; (c) at least one of the events occurs; (d) at least two of the events occur; (e) all three occur; (f ) none of the events occurs; (g) at most one of them occurs; (h) at most two of them occur; (i) exactly two of them occur; ( j) at most three of them occur.
## Dịch sang tiếng Việt
Gọi E, F, G là ba sự kiện. Tìm các biểu thức cho các sự kiện sau: (a) chỉ có E xảy ra; (b) cả E và G nhưng không có F xảy ra; (c) ít nhất một trong các sự kiện xảy ra; (d) ít nhất hai trong các sự kiện xảy ra; (e) cả ba sự kiện đều xảy ra; (f) không có sự kiện nào xảy ra; (g) nhiều nhất một trong số chúng xảy ra; (h) nhiều nhất hai trong số chúng xảy ra; (i) đúng hai trong số chúng xảy ra; (j) nhiều nhất ba trong số chúng xảy ra.
## Giải
- (a) Chỉ có E xảy ra: E ∩ F^c ∩ G^c
- (b) Cả E và G nhưng không có F xảy ra: E ∩ F^c ∩ G
- (c) Ít nhất một trong các sự kiện xảy ra: E ∪ F ∪ G
- (d) Ít nhất hai trong các sự kiện xảy ra: (E ∩ F) ∪ (E ∩ G) ∪ (F ∩ G)
- (e) Cả ba sự kiện đều xảy ra: E ∩ F ∩ G
- (f) Không có sự kiện nào xảy ra: E^c ∩ F^c ∩ G^c
- (g) Nhiều nhất một trong số chúng xảy ra: (E ∩ F^c ∩ G^c) ∪ (E^c ∩ F ∩ G^c) ∪ (E^c ∩ F^c ∩ G)
- (h) Nhiều nhất hai trong số chúng xảy ra: (E ∩ F ∩ G^c) ∪ (E ∩ F^c ∩ G) ∪ (E^c ∩ F ∩ G) ∪ (E^c ∩ F^c ∩ G^c)
- (i) Đúng hai trong số chúng xảy ra: (E ∩ F ∩ G^c) ∪ (E ∩ F^c ∩ G) ∪ (E^c ∩ F ∩ G)
- (j) Nhiều nhất ba trong số chúng xảy ra: Luôn đúng với mọi trường hợp vì có ba sự kiện.

# Ex7: Find simple expressions for the events (a) E ∪ E c ; (b) EE c ; (c) ( E ∪ F )( E ∪ F c ); (d) ( E ∪ F )( E c ∪ F )( E ∪ F c ); (e) ( E ∪ F )( F ∪ G ).
## Dịch sang tiếng Việt
Tìm các biểu thức đơn giản cho các sự kiện sau: (a) E ∪ E^c; (b) E E^c; (c) (E ∪ F)(E ∪ F^c); (d) (E ∪ F)(E^c ∪ F)(E ∪ F^c); (e) (E ∪ F)(F ∪ G).
## Giải
- (a) E ∪ E^c = Ω (tập không gian mẫu)
- (b) E E^c = ∅ (tập rỗng)
- (c) (E ∪ F)(E ∪ F^c) = E ∪ F
- (d) (E ∪ F)(E^c ∪ F)(E ∪ F^c) = (E ∪ F)(E ∪ F^c) = E ∪ F
- (e) (E ∪ F)(F ∪ G) = (E ∪ F ∪ G)

# Ex8: Use Venn diagrams (or any other method) to show that  (a) EF ⊂ E, E ⊂ E ∪ F;  (b) if E ⊂ F then Fc ⊂ Ec;  (c) the commutative laws are valid;  (d) the associative laws are valid;  (e) F = FE ∪ FEc;  (f ) E ∪ F = E ∪ EcF;  (g) DeMorgan’s laws are valid.
## Dịch sang tiếng Việt
Sử dụng sơ đồ Venn (hoặc bất kỳ phương pháp nào khác) để chứng minh rằng (a) EF ⊂ E, E ⊂ E ∪ F; (b) nếu E ⊂ F thì Fc ⊂ Ec; (c) các luật giao hoán là đúng; (d) các luật kết hợp là đúng; (e) F = FE ∪ FEc; (f) E ∪ F = E ∪ EcF; (g) các luật DeMorgan là đúng.
## Giải
- (a) EF ⊂ E: Mọi phần tử trong EF đều thuộc E. E ⊂ E ∪ F: Mọi phần tử trong E đều thuộc E ∪ F.
- (b) Nếu E ⊂ F thì mọi phần tử trong E đều thuộc F. Do đó, mọi phần tử không thuộc F (Fc) cũng không thuộc E (Ec), tức là Fc ⊂ Ec.
- (c) Luật giao hoán: E ∪ F = F ∪ E và EF = FE. Điều này đúng vì thứ tự của các sự kiện không ảnh hưởng đến kết quả của phép hợp hoặc giao.
- (d) Luật kết hợp: (E ∪ F) ∪ G = E ∪ (F ∪ G) và (EF)G = E(FG). Điều này đúng vì cách nhóm các sự kiện không ảnh hưởng đến kết quả của phép hợp hoặc giao.
- (e) F = FE ∪ FEc: Mọi phần tử trong F đều thuộc FE hoặc FEc, vì vậy F = FE ∪ FEc.
- (f) E ∪ F = E ∪ EcF: Mọi phần tử trong E ∪ F đều thuộc E hoặc EcF, vì vậy E ∪ F = E ∪ EcF.
- (g) Luật DeMorgan: (E ∪ F)c = Ec ∩ Fc và (EF)c = Ec ∪ Fc. Điều này đúng vì phần bù của hợp là giao của các phần bù, và phần bù của giao là hợp của các phần bù.

# Ex9: For  the  following  Venn  diagram,  describe  in  terms  of  E,  F,  and  G  the  events  denoted  in  the diagram by the Roman numerals I through VII.
## Dịch sang tiếng Việt
Đối với sơ đồ Venn sau, mô tả bằng các thuật ngữ E, F và G các sự kiện được biểu thị trong sơ đồ bằng các chữ số La Mã từ I đến VII.
## Giải
- I: E ∩ F^c ∩ G^c (Chỉ có E xảy ra)
- II: E ∩ F ∩ G^c (Cả E và F xảy ra, nhưng không có G)
- III: F ∩ E^c ∩ G^c (Chỉ có F xảy ra)
- IV: E ∩ F ∩ G (Cả E, F và G đều xảy ra)
- V: F ∩ G ∩ E^c (Cả F và G xảy ra, nhưng không có E)
- VI: G ∩ E^c ∩ F^c (Chỉ có G xảy ra)
- VII: E ∩ G ∩ F^c (Cả E và G xảy ra, nhưng không có F)

# Ex10: Show that if E⊂F then P(E) ≤ P(F ). (Hint: Write F as the union of two mutually exclusive events, one of them being E.)
## Dịch sang tiếng Việt
Chứng minh rằng nếu E ⊂ F thì P(E) ≤ P(F). (Gợi ý: Viết F như là hợp của hai sự kiện loại trừ lẫn nhau, một trong số đó là E.)
## Giải
- Giả sử E ⊂ F. Ta có thể viết F như sau:
  F = E ∪ (F ∩ E^c) 
- Áp dụng quy tắc xác suất cho hợp của hai sự kiện loại trừ lẫn nhau, ta có:
  P(F) = P(E) + P(F ∩ E^c)
- Vì P(F ∩ E^c) ≥ 0, nên P(F) ≥ P(E).
- Do đó, ta kết luận rằng nếu E ⊂ F thì P(E) ≤ P(F).

# Ex11: Prove Boole’s inequality, namely that
## Dịch sang tiếng Việt
Chứng minh bất đẳng thức của Boole, cụ thể là:
## Giải
- Phân rã thành các tập rời:
  - A1 = E1, A2 = E2 / E1, A3 = E3 / (E1 ∪ E2), ..., An = En / (E1 ∪ E2 ∪ ... ∪ E(n-1))
  - Ta có E1 ∪ E2 ∪ ... ∪ En = A1 ∪ A2 ∪ ... ∪ An
  - Do đó, P(E1 ∪ E2 ∪ ... ∪ En) = P(A1 ∪ A2 ∪ ... ∪ An) = P(A1) + P(A2) + ... + P(An) (vì các Ai là rời nhau)
  - Mỗi Ai là một phần của Ei, nên P(Ai) ≤ P(Ei)
  - Do đó, P(E1 ∪ E2 ∪ ... ∪ En) ≤ P(E1) + P(E2) + ... + P(En)

# Ex12: If P(E) = .9 and P(F ) = .9, show that P(EF) ≥.8. In general, prove Bonferroni’s inequality, namely that: P(EF) ≥ P(E) + P(F) - 1
## Dịch sang tiếng Việt
Nếu P(E) = 0.9 và P(F) = 0.9, chứng minh rằng P(EF) ≥ 0.8. Nói chung, chứng minh bất đẳng thức của Bonferroni, cụ thể là: P(EF) ≥ P(E) + P(F) - 1.
## Giải
- Áp dụng bất đẳng thức của Cauchy-Schwarz:
  P(EF) = P(E)P(F|E) ≥ P(E)P(F) = 0.9 * 0.9 = 0.81.
- Do đó, P(EF) ≥ 0.81 ≥ 0.8.
- Nói chung, bất đẳng thức của Bonferroni có thể được chứng minh bằng cách sử dụng nguyên lý bao hàm-exclusion.
- Ta có:
  P(E ∪ F) = P(E) + P(F) - P(EF) ≥ P(E) + P(F) - 1.
- Do đó, P(EF) ≥ P(E) + P(F) - 1.

# Ex13: Prove that: (a) P(EFc) = P(E) - P(EF); (b) P(EcFc) = 1 - P(E) - P(F) + P(EF)
## Dịch sang tiếng Việt
Chứng minh rằng: (a) P(EFc) = P(E) - P(EF); (b) P(EcFc) = 1 - P(E) - P(F) + P(EF).
## Giải
- (a) P(EFc) = P(E) - P(EF): Ta có P(E) = P(EF) + P(EFc), do đó P(EFc) = P(E) - P(EF).
- (b) P(EcFc) = 1 - P(E) - P(F) + P(EF): Ta có P(EcFc) = 1 - P(E ∪ F) = 1 - (P(E) + P(F) - P(EF)) = 1 - P(E) - P(F) + P(EF).

# Ex14: Show that the probability that exactly one of the events E or F occurs is equal to P(E) + P(F) - 2P(EF)
## Dịch sang tiếng Việt
Chứng minh rằng xác suất chỉ có một trong hai sự kiện E hoặc F xảy ra bằng P(E) + P(F) - 2P(EF).
## Giải
- Ta có:
  P(E ∩ F^c) = P(E) - P(EF)
  P(E^c ∩ F) = P(F) - P(EF)
- Do đó, xác suất chỉ có một trong hai sự kiện E hoặc F xảy ra là:
  P(E ∩ F^c) + P(E^c ∩ F) = (P(E) - P(EF)) + (P(F) - P(EF)) = P(E) + P(F) - 2P(EF).

# Ex15: Calculate 9C3, 9C6, 7C2, 7C5, 10C7.
## Dịch sang tiếng Việt
Tính 9C3, 9C6, 7C2, 7C5, 10C7.
## Giải
- 9C3 = 9! / (3!(9-3)!) = 84
- 9C6 = 9! / (6!(9-6)!) = 84
- 7C2 = 7! / (2!(7-2)!) = 21
- 7C5 = 7! / (5!(7-5)!) = 21
- 10C7 = 10! / (7!(10-7)!) = 120

# Ex16: Show that nCr = nC(n- r). Now present a combinatorial argument for the foregoing by explaining why a choice of  r  items from a set of size n is equivalent to a choice of n-r items from that set.
## Dịch sang tiếng Việt
Chứng minh rằng nCr = nC(n-r). Bây giờ hãy trình bày một lập luận tổ hợp cho điều trên bằng cách giải thích tại sao việc chọn r mục từ một tập hợp có kích thước n tương đương với việc chọn n-r mục từ tập hợp đó.
## Giải
- Việc chọn r mục từ n mục có thể được coi là việc chọn n-r mục không được chọn.
- Do đó, số cách chọn r mục từ n mục là bằng số cách chọn n-r mục không được chọn từ n mục.
- Điều này dẫn đến kết luận rằng nCr = nC(n-r).

# Ex17: Show that nCr = (n-1)C(r-1) + (n-1)Cr For a combinatorial argument, consider a set of n items and fix attention on one of these items. How many different sets of size r contain this item, and how many do not?
## Dịch sang tiếng Việt
Chứng minh rằng nCr = (n-1)C(r-1) + (n-1)Cr. Đối với một lập luận tổ hợp, hãy xem xét một tập hợp gồm n mục và cố định sự chú ý vào một trong những mục này.
Có bao nhiêu tập hợp khác nhau có kích thước r chứa mục này, và có bao nhiêu tập hợp không chứa nó?
## Giải
- Giả sử ta có n mục và ta đang xem xét một mục cụ thể trong số đó.
- Nếu tập hợp kích thước r chứa mục này, thì ta cần chọn (r-1) mục từ (n-1) mục còn lại.
- Do đó, số tập hợp kích thước r chứa mục này là (n-1)C(r-1).
- Nếu tập hợp kích thước r không chứa mục này, thì ta cần chọn tất cả r mục từ (n-1) mục còn lại.
- Do đó, số tập hợp kích thước r không chứa mục này là (n-1)Cr.
- Từ đó, ta có:
  nCr = (n-1)C(r-1) + (n-1)Cr.

# Ex18: A  group  of  5  boys  and  10  girls  is  lined  up  in  random  order  — that  is,  each  of  the  15! permutations is assumed to be equally likely. (a) What is the probability that the person in the 4th position is a boy? (b) What about the person in the 12th position? (c) What is the probability that a particular boy is in the 3rd position? 
## Dịch sang tiếng Việt
Một nhóm gồm 5 cậu bé và 10 cô bé được xếp thành hàng theo thứ tự ngẫu nhiên — tức là, mỗi trong số 15! hoán vị được giả định là có xác suất như nhau. (a) Xác suất để người ở vị trí thứ 4 là một cậu bé là bao nhiêu? (b) Còn người ở vị trí thứ 12 thì sao? (c) Xác suất để một cậu bé cụ thể ở vị trí thứ 3 là bao nhiêu?
## Giải
- (a) Xác suất để người ở vị trí thứ 4 là một cậu bé:
  - Tổng số cách xếp 15 người là 15!.
  - Số cách xếp sao cho người ở vị trí thứ 4 là một cậu bé là: Chọn 1 trong 5 cậu bé cho vị trí thứ 4 (5 cách), sau đó xếp 14 người còn lại (14! cách).
  - Do đó, xác suất là: P = (5 * 14!) / 15! = 5 / 15 = 1 / 3.
- (b) Xác suất để người ở vị trí thứ 12 là một cậu bé:
  - Tương tự như trên, số cách xếp sao cho người ở vị trí thứ 12 là một cậu bé là: Chọn 1 trong 5 cậu bé cho vị trí thứ 12 (5 cách), sau đó xếp 14 người còn lại (14! cách).
  - Do đó, xác suất là: P = (5 * 14!) / 15! = 5 / 15 = 1 / 3.
- (c) Xác suất để một cậu bé cụ thể ở vị trí thứ 3:
  - Số cách xếp sao cho cậu bé cụ thể ở vị trí thứ 3 là: Cố định cậu bé đó ở vị trí thứ 3, sau đó xếp 14 người còn lại (14! cách).
  - Do đó, xác suất là: P = 14! / 15! = 1 / 15.

# Ex19: Consider a set of 23 unrelated people. Because each pair of people shares thesame birthday with probability 1/365, and there are 23C2  = 253 pairs, why isn’t the probability thatat least two people have the same birthday equal to 253/365?
## Dịch sang tiếng Việt
Xem xét một tập hợp gồm 23 người không liên quan. Vì mỗi cặp người có xác suất chia sẻ cùng một ngày sinh là 1/365, và có 23C2 = 253 cặp, tại sao xác suất ít nhất hai người có cùng ngày sinh không bằng 253/365?
## Giải
- Xác suất ít nhất hai người có cùng ngày sinh là 1 trừ đi xác suất không ai có cùng ngày sinh.
- Xác suất không ai có cùng ngày sinh là: (365/365) * (364/365) * ... * (343/365) = 365! / (342! * 365^23).
- Do đó, xác suất ít nhất hai người có cùng ngày sinh là: 1 - (365! / (342! * 365^23)).
- Việc tính xác suất ít nhất hai người có cùng ngày sinh bằng 253/365 là sai vì nó giả định rằng các cặp người là độc lập với nhau, trong khi thực tế không phải vậy. Các cặp người có thể chia sẻ cùng một ngày sinh, làm tăng xác suất tổng thể.

# Ex20: Suppose  that  distinct  integer  values  are  written  on  each  of  3  cards.  These  cards  are  then randomly given the designations A, B, and C. The values on cards A and B are then compared. If the smaller of these values is then compared with the value on card C, what is the probability that it is also smaller than the value on card C?
## Dịch sang tiếng Việt
Giả sử các giá trị số nguyên khác nhau được viết trên mỗi trong số 3 thẻ. Các thẻ này sau đó được gán ngẫu nhiên các ký hiệu A, B và C. Giá trị trên thẻ A và B sau đó được so sánh. Nếu giá trị nhỏ hơn trong hai giá trị này sau đó được so sánh với giá trị trên thẻ C, xác suất để nó cũng nhỏ hơn giá trị trên thẻ C là bao nhiêu?
## Giải
- Gọi các giá trị trên thẻ là x1, x2, x3 với x1 < x2 < x3.
- Có 6 cách sắp xếp các thẻ A, B, C với các giá trị khác nhau:
  1. A = x1, B = x2, C = x3
  2. A = x1, B = x3, C = x2
  3. A = x2, B = x1, C = x3
  4. A = x2, B = x3, C = x1
  5. A = x3, B = x1, C = x2
  6. A = x3, B = x2, C = x1
- Trong các trường hợp 1, 3, và 5, giá trị nhỏ hơn giữa A và B là x1 hoặc x2, và nó sẽ luôn nhỏ hơn giá trị trên thẻ C (x3 hoặc x2).
- Do đó, có 3 trường hợp trong tổng số 6 trường hợp mà giá trị nhỏ hơn giữa A và B cũng nhỏ hơn giá trị trên thẻ C.
- Xác suất là: P = 3 / 6 = 1 / 2

# Ex21: There is a 60 percent chance that the event A will occur. If A does not occur, then there is a 10 percent chance that B will occur. (a) What is the probability that at least one of the events A or B occurs? (b) If A is the event that the democratic candidate wins the presidential election in 2012 and B is the event that there is a 6.2 or higher earthquake in Los Angeles sometime in 2013, what would you take as the probability that both A and B occur? What assumption are you making?
## Dịch sang tiếng Việt
Có 60% khả năng sự kiện A xảy ra. Nếu A không xảy ra, thì có 10% khả năng sự kiện B xảy ra. (a) Xác suất để ít nhất một trong hai sự kiện A hoặc B xảy ra là bao nhiêu? (b) Nếu A là sự kiện ứng cử viên Đảng Dân chủ thắng cử tổng thống năm 2012 và B là sự kiện có một trận động đất 6.2 hoặc lớn hơn ở Los Angeles vào một thời điểm nào đó trong năm 2013, bạn sẽ lấy xác suất để cả A và B cùng xảy ra là bao nhiêu? Bạn đang giả định điều gì?
## Giải
- Cho biết: P(A) = 0.6; P(B | A^c) = 0.1; do đó P(A^c) = 0.4.
- (a) Ta có thể tính trực tiếp:
  - P(A ∪ B) = P(A) + P(B ∩ A^c) = 0.6 + P(B | A^c)P(A^c) = 0.6 + 0.1·0.4 = 0.64.
- (b) Với hai sự kiện thuộc các lĩnh vực không liên quan (kết quả bầu cử và hoạt động địa chấn), cách tự nhiên là giả định độc lập, khi đó
  - P(A ∩ B) = P(A)P(B).
  - Giả định đang dùng: A và B độc lập (kết quả bầu cử không ảnh hưởng đến xác suất có động đất, và ngược lại). Lưu ý: Giá trị cụ thể cần thêm ước lượng/nguồn cho P(B).

# Ex22: The sample mean of the annual salaries of a group of 100 accountants who work at a large accounting firm is $130,000 with a sample standard deviation of $20,000. If a member of this group is randomly chosen, what can we say about (a) the probability that his or her salary is between $90,000 and $170,000? (b) the probability that his or her salary exceeds $150,000? Hint: Use the Chebyshev inequality.
## Dịch sang tiếng Việt
Trung bình mẫu của mức lương hằng năm của một nhóm 100 kế toán làm việc tại một công ty kiểm toán lớn là $130.000 với độ lệch chuẩn mẫu là $20.000. Nếu ngẫu nhiên chọn một người trong nhóm này, ta có thể nói gì về (a) xác suất lương của người đó nằm giữa $90.000 và $170.000? (b) xác suất lương của người đó vượt quá $150.000? Gợi ý: Dùng bất đẳng thức Chebyshev.
## Giải
- Gọi X là mức lương của một người bất kỳ trong nhóm. Ta dùng trung bình mẫu và độ lệch chuẩn mẫu như ước lượng cho kỳ vọng μ ≈ 130.000 và độ lệch chuẩn σ ≈ 20.000.
- (a) Khoảng $90.000 đến $170.000 tương ứng |X − μ| ≤ 40.000 = 2σ. Áp dụng Chebyshev hai phía:
  - P(|X − μ| < kσ) ≥ 1 − 1/k^2, với k = 2 ⇒ P(90.000 ≤ X ≤ 170.000) ≥ 1 − 1/2^2 = 3/4 = 0.75.
  - Kết luận: Xác suất ít nhất là 0.75.
- (b) Mức $150.000 là μ + 20.000 = μ + 1σ. Chebyshev hai phía chỉ cho chặn trên tầm thường P(X ≥ μ + σ) ≤ 1. Để có chặn ý nghĩa cho phía trên, dùng bản một phía (Cantelli’s inequality, còn gọi là Chebyshev một phía):
  - P(X − μ ≥ t) ≤ σ^2 / (σ^2 + t^2). Với t = 20.000: P(X ≥ 150.000) ≤ (20.000)^2 / ((20.000)^2 + (20.000)^2) = 1/2 = 0.5.
  - Kết luận: Xác suất lương vượt $150.000 không quá 0.5 (theo chặn Cantelli).
- Lưu ý: Đây là các bất đẳng thức (chặn trên/dưới), không phải giá trị chính xác, và ta đã ngầm dùng thống kê mẫu làm xấp xỉ cho tham số quần thể.

# Ex23: Of three cards, one is painted red on both sides; one is painted black on both sides; and one is painted red on one side and black on the other. A card is randomly chosen and placed on a table. If the side facing up is red, what is the probability that the other side is also red?
## Dịch sang tiếng Việt
Trong ba tấm thẻ: một thẻ sơn đỏ cả hai mặt; một thẻ sơn đen cả hai mặt; và một thẻ sơn đỏ một mặt, đen mặt kia. Chọn ngẫu nhiên một thẻ và đặt lên bàn. Biết rằng mặt quay lên là màu đỏ, hỏi xác suất mặt còn lại cũng là màu đỏ là bao nhiêu?
## Giải
- Liệt kê các mặt có thể nhìn thấy khi rút và đặt ngẫu nhiên: RR có 2 mặt đỏ; BB có 2 mặt đen; RB có 1 mặt đỏ và 1 mặt đen. Tổng số mặt khả dĩ là 2 + 2 + 2 = 6, trong đó các mặt đỏ là: 2 (từ RR) + 1 (từ RB) = 3.
- Điều kiện mặt trên là đỏ ⇒ không gian điều kiện gồm 3 mặt đỏ khả dĩ: {R_R từ RR (2 khả năng khác nhau), R từ RB (1 khả năng)}.
- Xác suất mặt dưới cũng đỏ chỉ xảy ra khi thẻ là RR, tức 2 trong 3 khả năng đỏ.
- Vậy P = 2/3.

# Ex24: A couple has 2 children. What is the probability that both are girls if the eldest is a girl?
## Dịch sang tiếng Việt
Một cặp vợ chồng có 2 con. Xác suất cả hai đều là gái nếu biết người con lớn là gái?
## Giải
- Không gian mẫu theo thứ tự (Lớn, Bé): {BB, BG, GB, GG}, mỗi kết quả xác suất 1/4, giả sử trai/gái độc lập và xác suất 1/2–1/2.
- Điều kiện “con lớn là gái” loại bỏ các trường hợp có con lớn là trai ⇒ còn {GB, GG} với xác suất có điều kiện đều nhau.
- Xác suất cả hai là gái = P(GG | con lớn là gái) = 1/2.

# Ex25: Fifty-two percent of the students at a certain college are females. Five percent of the students in this college are majoring in computer science. Two percent of the students are women majoring in computer science. If a student is selected at random, find the conditional probability that (a) this student is female, given that the student is majoring in computer science; (b) this student is majoring in computer science, given that the student is female.
## Dịch sang tiếng Việt
52% sinh viên của một trường đại học là nữ. 5% sinh viên chuyên ngành khoa học máy tính (CS). 2% sinh viên là nữ và chuyên ngành CS. Nếu chọn ngẫu nhiên một sinh viên, hãy tìm xác suất có điều kiện: (a) người này là nữ, biết rằng người đó học CS; (b) người này học CS, biết rằng người đó là nữ.
## Giải
- Ký hiệu: F = “nữ”, C = “học CS”. Cho biết P(F) = 0.52, P(C) = 0.05, P(F ∩ C) = 0.02.
- (a) P(F | C) = P(F ∩ C) / P(C) = 0.02 / 0.05 = 0.4.
- (b) P(C | F) = P(F ∩ C) / P(F) = 0.02 / 0.52 ≈ 0.03846 ≈ 3.846%.

# Ex26: A total of 500 married working couples were polled about their annual salaries, with the following information resulting.

|                | Husband < $50,000 | Husband ≥ $50,000 |
|----------------|-------------------|-------------------|
| Wife < $50,000 | 212               | 198               |
| Wife ≥ $50,000 | 36                | 54                |

Thus, for instance, in 36 of the couples the wife earned more and the husband earned less than $50,000. If one of the couples is randomly chosen, what is
(a) the probability that the husband earns less than $50,000;
(b) the conditional probability that the wife earns more than $50,000 given that the husband earns more than this amount;
(c) the conditional probability that the wife earns more than $50,000 given that the husband earns less than this amount?
## Dịch sang tiếng Việt
Khảo sát 500 cặp vợ chồng (cả hai cùng đi làm) về mức lương năm, thu được bảng sau.

|                | Chồng < $50,000 | Chồng ≥ $50,000 |
|----------------|------------------|------------------|
| Vợ < $50,000   | 212              | 198              |
| Vợ ≥ $50,000   | 36               | 54               |

Ví dụ, có 36 cặp mà vợ kiếm nhiều hơn $50,000 còn chồng kiếm ít hơn $50,000. Chọn ngẫu nhiên một cặp, hãy tính:
(a) xác suất chồng kiếm < $50,000;
(b) xác suất có điều kiện vợ kiếm ≥ $50,000 biết rằng chồng kiếm ≥ $50,000;
(c) xác suất có điều kiện vợ kiếm ≥ $50,000 biết rằng chồng kiếm < $50,000.
## Giải
- Tổng cộng N = 500. Tính các tổng hàng/cột:
  - Chồng < 50k: 212 + 36 = 248; Chồng ≥ 50k: 198 + 54 = 252.
  - Vợ < 50k: 212 + 198 = 410; Vợ ≥ 50k: 36 + 54 = 90.
- (a) P(Chồng < 50k) = 248/500 = 0.496.
- (b) P(Vợ ≥ 50k | Chồng ≥ 50k) = 54 / 252 = 3/14 ≈ 0.2143.
- (c) P(Vợ ≥ 50k | Chồng < 50k) = 36 / 248 = 9/62 ≈ 0.1452.

# Ex27: There are two local factories that produce microwaves. Each microwave produced at factory A is defective with probability .05, whereas each one produced at factory B is defective with probability .01. Suppose you purchase two microwaves that were produced at the same factory, which is equally likely to have been either factory A or factory B. If the first microwave that you check is defective, what is the conditional probability that the other one is also defective?
## Dịch sang tiếng Việt
Có hai nhà máy địa phương sản xuất lò vi sóng. Mỗi lò từ nhà máy A bị lỗi với xác suất 0.05, còn mỗi lò từ nhà máy B bị lỗi với xác suất 0.01. Giả sử bạn mua hai lò được sản xuất từ cùng một nhà máy, và khả năng thuộc A hay B là như nhau. Nếu chiếc đầu tiên kiểm tra bị lỗi, xác suất có điều kiện để chiếc còn lại cũng bị lỗi là bao nhiêu?
## Giải
- Ký hiệu F ∈ {A, B} là nhà máy; P(F=A) = P(F=B) = 1/2. Cho rằng, với cùng nhà máy F, hai sản phẩm độc lập và có xác suất lỗi p_A = 0.05, p_B = 0.01.
- Ta cần P(D2 = 1 | D1 = 1). Sử dụng Bayes theo nhà máy:
  - P(F=A | D1) = [P(D1|A)P(A)] / [P(D1|A)P(A) + P(D1|B)P(B)] = (0.05·0.5)/(0.05·0.5 + 0.01·0.5) = 5/6.
  - P(F=B | D1) = 1/6.
  - Khi biết F, D2 độc lập với D1 và P(D2=1|F) = p_F. Do đó
    P(D2=1 | D1=1) = (5/6)·0.05 + (1/6)·0.01 = 0.043333… = 13/300.
- Cách khác: P(D2=1 | D1=1) = P(D1=1, D2=1)/P(D1=1) = [0.5·0.05^2 + 0.5·0.01^2] / [0.5·0.05 + 0.5·0.01] = 0.0013/0.03 = 13/300.

# Ex28: A red die, a blue die, and a yellow die (all six-sided) are rolled. We are interested in the probability that the number appearing on the blue die is less than that appearing on the yellow die which is less than that appearing on the red die, i.e., P(B < Y < R).
(a) What is the probability that no two of the dice land on the same number?
(b) Given that no two of the dice land on the same number, what is P(B < Y < R | all different)?
(c) What is P(B < Y < R)?
(d) If we regard the outcome of the experiment as the vector (B, R, Y), how many outcomes are there in the sample space?
(e) Without using the answer to (c), determine the number of outcomes that result in B < Y < R.
(f) Use the results of (d) and (e) to verify (c).
## Dịch sang tiếng Việt
Một xúc xắc đỏ, một xúc xắc xanh dương và một xúc xắc vàng (đều 6 mặt) được tung. Ta quan tâm đến xác suất P(B < Y < R).
(a) Xác suất không có hai xúc xắc nào ra cùng số?
(b) Với điều kiện ba giá trị đều khác nhau, xác suất P(B < Y < R | khác nhau) là bao nhiêu?
(c) Tính P(B < Y < R).
(d) Nếu coi kết quả là véc-tơ (B, R, Y), có bao nhiêu kết cục trong không gian mẫu?
(e) Không dùng đáp án (c), hãy đếm số kết cục thỏa B < Y < R.
(f) Dùng (d) và (e) để kiểm chứng (c).
## Giải
- (a) Tổng số kết cục: 6^3 = 216. Số trường hợp ba giá trị khác nhau: 6·5·4 = 120. Do đó P(all different) = 120/216 = 5/9.
- (b) Khi đã khác nhau, ba giá trị phân biệt có 3! = 6 thứ tự đều nhau; chỉ 1 thứ tự thỏa B < Y < R ⇒ P = 1/6.
- (c) P(B < Y < R) = P(all different)·P(B < Y < R | all different) = (120/216)·(1/6) = 20/216 = 5/54.
- (d) Kích thước không gian mẫu cho (B, R, Y): 6·6·6 = 216.
- (e) Chọn bộ ba giá trị tăng dần {b < y < r} từ {1,…,6}: C(6,3) = 20; với mỗi bộ, đúng 1 hoán vị cho (B, Y, R) theo thứ tự tăng ⇒ số kết cục = 20.
- (f) Xác suất = số kết cục thuận lợi / tổng số kết cục = 20 / 216 = 5/54, trùng với (c).

# Ex29: You ask your neighbor to water a sickly plant while you are on vacation. Without water it will die with probability .8; with water it will die with probability .15. You are 90 percent certain that your neighbor will remember to water the plant. (a) What is the probability that the plant will be alive when you return? (b) If it is dead, what is the probability your neighbor forgot to water it?
## Dịch sang tiếng Việt
Bạn nhờ hàng xóm tưới một cây đang yếu trong thời gian bạn đi nghỉ. Không được tưới thì cây chết với xác suất 0.8; được tưới thì chết với xác suất 0.15. Bạn chắc 90% rằng hàng xóm sẽ nhớ tưới cây. (a) Xác suất cây còn sống khi bạn về là bao nhiêu? (b) Nếu cây đã chết, xác suất hàng xóm quên tưới là bao nhiêu?
## Giải
- Ký hiệu W: được tưới; P(W) = 0.9, P(W^c) = 0.1. Cho biết P(dead | W) = 0.15 ⇒ P(alive | W) = 0.85; P(dead | W^c) = 0.8 ⇒ P(alive | W^c) = 0.2.
- (a) P(alive) = P(W)P(alive|W) + P(W^c)P(alive|W^c) = 0.9·0.85 + 0.1·0.2 = 0.785.
- (b) P(W^c | dead) = [P(dead|W^c)P(W^c)] / P(dead), trong đó P(dead) = 0.9·0.15 + 0.1·0.8 = 0.215.
  - Suy ra P(W^c | dead) = 0.08 / 0.215 = 80/215 = 16/43 ≈ 0.3721.

# Ex30: Two balls, each equally likely to be colored either red or blue, are put in an urn. At each stage one of the balls is randomly chosen, its color is noted, and it is then returned to the urn. If the first two balls chosen are colored red, what is the probability that (a) both balls in the urn are colored red; (b) the next ball chosen will be red?
## Dịch sang tiếng Việt
Hai quả bóng, mỗi quả có khả năng bằng nhau để được tô đỏ hoặc xanh, được bỏ vào một bình. Mỗi lượt rút ngẫu nhiên một quả, ghi nhận màu rồi trả lại. Nếu hai lần rút đầu đều thấy đỏ, hỏi xác suất: (a) cả hai quả trong bình đều đỏ; (b) lần rút tiếp theo là đỏ?
## Giải
- Gọi thành phần bình có thể là RR, RB, BB với xác suất tiên nghiệm: P(RR)=1/4, P(RB)=1/2, P(BB)=1/4 (hai bóng độc lập, mỗi bóng đỏ với xác suất 1/2).
- Xác suất thấy đỏ ở mỗi lần rút theo từng thành phần: RR ⇒ 1; RB ⇒ 1/2; BB ⇒ 0. Với thay thế, hai lần độc lập theo thành phần ⇒ P(đỏ, đỏ | RR=1, |RB=1/4, |BB=0).
- Hậu nghiệm sau khi quan sát (đỏ, đỏ):
  - P(RR | đỏ,đỏ) ∝ (1/4)·1 = 1/4; P(RB | đỏ,đỏ) ∝ (1/2)·(1/4) = 1/8; P(BB | đỏ,đỏ)=0.
  - Chuẩn hóa: tổng 1/4+1/8=3/8 ⇒ P(RR|obs)= (1/4)/(3/8) = 2/3; P(RB|obs)= 1/3.
- (a) P(cả hai đỏ | đã thấy đỏ, đỏ) = 2/3.
- (b) P(lần sau đỏ | đã thấy đỏ, đỏ) = P(RR|obs)·1 + P(RB|obs)·(1/2) = (2/3) + (1/3)(1/2) = 5/6.

# Ex31: A total of 600 of the 1,000 people in a retirement community classify themselves as Republicans, while the others classify themselves as Democrats. In a local election in which everyone voted, 60 Republicans voted for the Democratic candidate, and 50 Democrats voted for the Republican candidate. If a randomly chosen community member voted for the Republican, what is the probability that she or he is a Democrat?
## Dịch sang tiếng Việt
Trong một cộng đồng hưu trí có 1.000 người, 600 người tự nhận là Đảng Cộng hòa (R), số còn lại là Đảng Dân chủ (D). Trong một cuộc bầu cử địa phương mà mọi người đều đi bầu, có 60 người R bỏ phiếu cho ứng viên D, và 50 người D bỏ phiếu cho ứng viên R. Nếu chọn ngẫu nhiên một người và biết người đó đã bầu cho ứng viên R, xác suất người đó là D là bao nhiêu?
## Giải
- Số R bầu cho R: 600 − 60 = 540. Số D bầu cho R: 50. Tổng số phiếu cho R: 540 + 50 = 590.
- Xác suất yêu cầu: P(D | vote R) = 50 / 590 = 5/59 ≈ 0.08475.

# Ex32: Each of 2 balls is painted black or gold and then placed in an urn. Suppose that each ball is colored black with probability 1/2, independently. (a) Suppose that you obtain information that the gold paint has been used (that is, at least one ball is gold). Compute the conditional probability that both balls are gold. (b) Suppose now that the urn tips over and 1 ball falls out. It is painted gold. What is the probability that both balls are gold in this case? Explain.
## Dịch sang tiếng Việt
Mỗi trong 2 quả bóng được tô đen hoặc vàng rồi bỏ vào bình. Mỗi bóng có xác suất 1/2 là màu đen, độc lập. (a) Biết rằng đã dùng sơn vàng (tức ít nhất một bóng là vàng). Tính xác suất có điều kiện rằng cả hai đều vàng. (b) Bình bị đổ và 1 bóng rơi ra; đó là bóng màu vàng. Khi đó xác suất cả hai bóng đều vàng là bao nhiêu? Giải thích.
## Giải
- Phân bố tiên nghiệm: BB: 1/4, BG: 1/2, GG: 1/4.
- (a) Điều kiện “ít nhất một bóng vàng” có xác suất 1 − P(BB) = 3/4. Do đó
  - P(GG | ≥1 vàng) = (1/4) / (3/4) = 1/3.
- (b) Sự kiện quan sát “một bóng rơi ra và nó là vàng” có xác suất theo từng cấu hình: GG → 1; GB → 1/2; BB → 0. Bằng Bayes:
  - Tỷ lệ hậu nghiệm ∝ tiên nghiệm × khả năng: GG: (1/4)·1 = 1/4; GB: (1/2)·(1/2) = 1/4.
  - Chuẩn hóa cho tổng 1/2 ⇒ P(GG | rơi ra là vàng) = (1/4)/(1/2) = 1/2.
  - Khác biệt với (a) vì “thấy một bóng vàng cụ thể” cung cấp thông tin mạnh hơn “ít nhất một vàng”.

# Ex33: Each of 2 cabinets identical in appearance has 2 drawers. Cabinet A contains a silver coin in each drawer, and cabinet B contains a silver coin in one of its drawers and a gold coin in the other. A cabinet is randomly selected, one of its drawers is opened, and a silver coin is found. What is the probability that there is a silver coin in the other drawer?
## Dịch sang tiếng Việt
Hai tủ giống hệt nhau, mỗi tủ có 2 ngăn. Tủ A có đồng bạc (S) ở cả hai ngăn; tủ B có một đồng bạc và một đồng vàng (G). Chọn ngẫu nhiên một tủ, mở ngẫu nhiên một ngăn và thấy đồng bạc. Xác suất ngăn còn lại cũng chứa đồng bạc là bao nhiêu?
## Giải
- P(A) = P(B) = 1/2. Xác suất thấy bạc: P(S | A) = 1; P(S | B) = 1/2.
- Bayes: P(A | S) ∝ (1/2)·1 = 1/2; P(B | S) ∝ (1/2)·(1/2) = 1/4 ⇒ chuẩn hóa: P(A|S) = (1/2)/(3/4) = 2/3; P(B|S) = 1/3.
- Nếu là tủ A thì ngăn còn lại chắc chắn là bạc; nếu là tủ B thì ngăn còn lại là vàng. Vậy xác suất yêu cầu = 2/3.

# Ex34: Prostate cancer is the most common type of cancer found in males. As an indicator of whether a male has prostate cancer, doctors often perform a test that measures the level of the PSA protein (prostate specific antigen) that is produced only by the prostate gland. Although higher PSA levels are indicative of cancer, the test is notoriously unreliable. Indeed, the probability that a noncancerous man will have an elevated PSA level is approximately .135, with this probability increasing to approximately .268 if the man does have cancer. If, based on other factors, a physician is 70 percent certain that a male has prostate cancer, what is the conditional probability that he has the cancer given that (a) the test indicates an elevated PSA level; (b) the test does not indicate an elevated PSA level? Repeat the preceding, this time assuming that the physician initially believes there is a 30 percent chance the man has prostate cancer.
## Dịch sang tiếng Việt
Ung thư tuyến tiền liệt là loại ung thư phổ biến nhất ở nam giới. Để chỉ báo người nam có ung thư hay không, bác sĩ thường làm xét nghiệm đo mức PSA (prostate specific antigen) do tuyến tiền liệt tiết ra. Dù PSA cao gợi ý ung thư, xét nghiệm này nổi tiếng là không đáng tin. Xác suất một người không mắc ung thư vẫn có PSA tăng là khoảng 0.135; nếu người đó mắc ung thư thì xác suất có PSA tăng là khoảng 0.268. Nếu dựa trên yếu tố khác, bác sĩ tin 70% rằng người nam có ung thư, hãy tính xác suất có điều kiện rằng người đó thực sự có ung thư khi (a) xét nghiệm cho thấy PSA tăng; (b) xét nghiệm không cho thấy PSA tăng. Lặp lại các câu hỏi trên nhưng giả sử ban đầu bác sĩ tin chỉ có 30% khả năng người này có ung thư.
## Giải
- Ký hiệu C: có ung thư; T: PSA tăng (test dương). Cho: P(T|C)=0.268; P(T|C^c)=0.135; nên P(T^c|C)=0.732; P(T^c|C^c)=0.865.
- Trường hợp prior 70%: P(C)=0.7, P(C^c)=0.3.
  - (a) P(C|T) = [P(T|C)P(C)] / [P(T|C)P(C)+P(T|C^c)P(C^c)] = (0.268·0.7)/(0.268·0.7 + 0.135·0.3).
    = 0.1876 / (0.1876 + 0.0405) = 0.1876 / 0.2281 ≈ 0.8227.
  - (b) P(C|T^c) = [P(T^c|C)P(C)] / [P(T^c|C)P(C)+P(T^c|C^c)P(C^c)] = (0.732·0.7)/(0.732·0.7 + 0.865·0.3).
    = 0.5124 / (0.5124 + 0.2595) = 0.5124 / 0.7719 ≈ 0.6639.
- Trường hợp prior 30%: P(C)=0.3, P(C^c)=0.7.
  - (a) P(C|T) = (0.268·0.3)/(0.268·0.3 + 0.135·0.7) = 0.0804 / (0.0804 + 0.0945) = 0.0804 / 0.1749 ≈ 0.4596.
  - (b) P(C|T^c) = (0.732·0.3)/(0.732·0.3 + 0.865·0.7) = 0.2196 / (0.2196 + 0.6055) = 0.2196 / 0.8251 ≈ 0.2662.
 - Nhận xét: Vì test khá kém (tỷ lệ dương giả 13.5% và nhạy 26.8% thấp), kết quả dương không nâng xác suất lên quá cao nếu prior thấp, và kết quả âm vẫn để lại xác suất hậu nghiệm đáng kể nếu prior cao.

# Ex35: Suppose that an insurance company classifies people into one of three classes — good risks, average risks, and bad risks. Their records indicate that the probabilities that good, average, and bad risk persons will be involved in an accident over a 1-year span are, respectively, .05, .15, and .30. If 20 percent of the population are “good risks,” 50 percent are “average risks,” and 30 percent are “bad risks,” what proportion of people have accidents in a fixed year? If policy holder A had no accidents in 1987, what is the probability that he or she is a good (average) risk?
## Dịch sang tiếng Việt
Giả sử một công ty bảo hiểm phân loại người thành ba nhóm — rủi ro tốt, trung bình, và xấu. Hồ sơ cho biết xác suất tham gia tai nạn trong một năm đối với từng nhóm lần lượt là 0.05, 0.15, 0.30. Nếu 20% dân số là nhóm tốt, 50% nhóm trung bình, 30% nhóm xấu, hỏi tỷ lệ người gặp tai nạn trong một năm cố định là bao nhiêu? Nếu người mua bảo hiểm A không gặp tai nạn trong năm 1987, xác suất A thuộc nhóm tốt (trung bình) là bao nhiêu?
## Giải
- Ký hiệu lớp: G (tốt), M (trung bình), B (xấu). Phân bố tiên nghiệm: P(G)=0.2, P(M)=0.5, P(B)=0.3.
- Xác suất tai nạn theo lớp: p_G=0.05, p_M=0.15, p_B=0.30. Không tai nạn: q_i=1-p_i.
- Tỷ lệ dân số có tai nạn trong năm: P(Acc)=∑ P(class)·p_class = 0.2·0.05 + 0.5·0.15 + 0.3·0.30 = 0.01 + 0.075 + 0.09 = 0.175.
- Cho biết A không tai nạn (N). Khi đó
  - P(G|N) ∝ P(G)·q_G = 0.2·0.95 = 0.19
  - P(M|N) ∝ 0.5·0.85 = 0.425
  - P(B|N) ∝ 0.3·0.70 = 0.21
  - Tổng chuẩn hóa S = 0.19 + 0.425 + 0.21 = 0.825.
  - P(G|N) = 0.19 / 0.825 ≈ 0.2303; P(M|N) = 0.425 / 0.825 ≈ 0.5152.

# Ex36: A pair of fair dice is rolled. Let E denote the event that the sum of the dice is equal to 7. (a) Show that E is independent of the event that the first die lands on 4. (b) Show that E is independent of the event that the second die lands on 3.
## Dịch sang tiếng Việt
Tung hai con xúc xắc công bằng. Gọi E là sự kiện tổng bằng 7. (a) Chứng minh E độc lập với sự kiện “xúc xắc thứ nhất ra 4”. (b) Chứng minh E độc lập với sự kiện “xúc xắc thứ hai ra 3”.
## Giải
- Không gian mẫu 36 kết cục đều nhau. Gọi A = {đi 1 = 4}, B = {đi 2 = 3}.
- P(E) = 6/36 = 1/6 vì các cặp tổng 7 là (1,6),(2,5),(3,4),(4,3),(5,2),(6,1).
- P(A) = 6/36 = 1/6; P(B) = 6/36 = 1/6.
- (a) E ∩ A xảy ra khi (4,3) ⇒ P(E∩A) = 1/36 = P(E)P(A) = (1/6)(1/6).
- (b) E ∩ B xảy ra khi (4,3) ⇒ P(E∩B) = 1/36 = P(E)P(B) = (1/6)(1/6).
- Do đó E độc lập với cả A và B.

# Ex37: The probability of the closing of the ith relay in the circuits shown is given by p_i, i = 1, 2, 3, 4, 5. If all relays function independently, what is the probability that a current flows between A and B for the respective circuits?
## Dịch sang tiếng Việt
Xác suất tiếp điểm i (i = 1, 2, 3, 4, 5) đóng là p_i. Giả sử các rơ-le hoạt động độc lập. Hãy tính xác suất có dòng điện chạy từ A đến B đối với từng sơ đồ (a), (b), (c).
## Giải
- Ký hiệu p_i = P(rơ-le i đóng), độc lập nhau.

### (a) Hai nhánh song song: nhánh trên là 1–2–3 nối tiếp; nhánh dưới là 4–5 nối tiếp.
- Xác suất nhánh trên dẫn: p_1 p_2 p_3. Nhánh dưới dẫn: p_4 p_5.
- Toàn mạch dẫn khi ít nhất một nhánh dẫn: P = 1 − (1 − p_1 p_2 p_3)(1 − p_4 p_5) = p_1 p_2 p_3 + p_4 p_5 − p_1 p_2 p_3 p_4 p_5.

### (b) Hai nhánh song song (1–2 và 3–4) nối tiếp với 5.
- Khối trái (từ A đến nút bên phải) dẫn nếu (1–2) hoặc (3–4) dẫn: P_block = 1 − (1 − p_1 p_2)(1 − p_3 p_4).
- Toàn mạch cần thêm 5 đóng (nối tiếp): P = p_5 · P_block = p_5 · [1 − (1 − p_1 p_2)(1 − p_3 p_4)].

### (c) Mạch cầu (kim cương) với nhánh giữa là 3.
- Điều kiện theo rơ-le 3:
  - Nếu 3 đóng (xác suất p_3): hai nút giữa được nối lại thành một. Khi đó từ A đến nút giữa là song song (1 ∪ 2), và từ nút giữa đến B là song song (4 ∪ 5). Do độc lập và tách rời hai cụm này:
    P(E | 3 đóng) = [1 − (1 − p_1)(1 − p_2)] · [1 − (1 − p_4)(1 − p_5)].
  - Nếu 3 hở (xác suất 1 − p_3): chỉ còn hai đường độc lập 1–4 và 2–5 song song:
    P(E | 3 hở) = 1 − (1 − p_1 p_4)(1 − p_2 p_5) = p_1 p_4 + p_2 p_5 − p_1 p_2 p_4 p_5.
- Suy ra xác suất dẫn của toàn mạch:
  P = p_3 · [1 − (1 − p_1)(1 − p_2)] · [1 − (1 − p_4)(1 − p_5)]
      + (1 − p_3) · [p_1 p_4 + p_2 p_5 − p_1 p_2 p_4 p_5].

# Ex38: An engineering system consisting of n components is said to be a k-out-of-n system (k ≤ n) if the system functions if and only if at least k of the n components function. Suppose that all components function independently of each other. (a) If the ith component functions with probability P_i, i = 1, 2, 3, 4, compute the probability that a 2-out-of-4 system functions. (b) Repeat (a) for a 3-out-of-5 system.
## Dịch sang tiếng Việt
Một hệ thống gồm n linh kiện gọi là hệ k-trong-n (k ≤ n) nếu hệ hoạt động khi và chỉ khi có ít nhất k trong n linh kiện hoạt động. Giả sử các linh kiện hoạt động độc lập. (a) Với 4 linh kiện có xác suất hoạt động P_i (i=1..4), hãy tính xác suất hệ 2-trong-4 hoạt động. (b) Lặp lại cho hệ 3-trong-5.
## Giải
- Ký hiệu P_i = P(thành phần i hoạt động), độc lập nhau. Hệ k-trong-n hoạt động khi có ≥ k thành phần hoạt động.
- (a) 2-trong-4: P(hệ hoạt động) = 1 − P(0 hoạt động) − P(chỉ 1 hoạt động).
  - P(0) = ∏_{i=1}^4 (1 − P_i).
  - P(chỉ 1) = ∑_{i=1}^4 P_i · ∏_{j≠i} (1 − P_j).
  - Suy ra: P_2of4 = 1 − ∏_{i=1}^4(1−P_i) − ∑_{i=1}^4 P_i ∏_{j≠i}(1−P_j).
  - Trường hợp đồng nhất P_i = p: P_2of4 = C(4,2)p^2(1−p)^2 + C(4,3)p^3(1−p) + C(4,4)p^4 = 6p^2(1−p)^2 + 4p^3(1−p) + p^4.
- (b) 3-trong-5: P(hệ hoạt động) = 1 − P(0) − P(1) − P(2).
  - P(0) = ∏_{i=1}^5 (1 − P_i).
  - P(1) = ∑_{i=1}^5 P_i ∏_{j≠i} (1 − P_j).
  - P(2) = ∑_{1≤i<j≤5} P_i P_j ∏_{ℓ∉{i,j}} (1 − P_ℓ).
  - Suy ra: P_3of5 = 1 − ∏_{i=1}^5(1−P_i) − ∑_{i=1}^5 P_i ∏_{j≠i}(1−P_j) − ∑_{i<j} P_i P_j ∏_{ℓ∉{i,j}} (1−P_ℓ).
  - Trường hợp đồng nhất P_i = p: P_3of5 = C(5,3)p^3(1−p)^2 + C(5,4)p^4(1−p) + C(5,5)p^5 = 10p^3(1−p)^2 + 5p^4(1−p) + p^5.

# Ex39: Five independent flips of a fair coin are made. Find the probability that (a) the first three flips are the same; (b) either the first three flips are the same, or the last three flips are the same; (c) there are at least two heads among the first three flips, and at least two tails among the last three flips.
## Dịch sang tiếng Việt
Tung đồng xu công bằng 5 lần độc lập. Tính xác suất: (a) ba lần đầu giống nhau; (b) hoặc ba lần đầu giống nhau, hoặc ba lần cuối giống nhau; (c) có ít nhất hai mặt ngửa trong ba lần đầu và ít nhất hai mặt sấp trong ba lần cuối.
## Giải
- Ký hiệu H/T cho ngửa/sấp, mỗi lần P(H)=P(T)=1/2.
- (a) Ba lần đầu giống nhau: hoặc HHH hoặc TTT. Xác suất = 2·(1/2)^3 = 1/4.
- (b) Gọi A: ba lần đầu giống nhau (P=1/4); B: ba lần cuối giống nhau (P=1/4).
  - P(A∪B) = P(A)+P(B)−P(A∩B).
  - P(A∩B): cả ba đầu giống nhau và ba cuối giống nhau. Hai khối (1–3) và (3–5) giao nhau tại lần 3, nhưng có thể đếm trực tiếp theo chuỗi 5 bit.
    + Trường hợp HHH ở 1–3: để 3–5 giống nhau, (3,4,5) phải HHH hoặc TTT. Với 3 đã là H, 3–5 = HHH buộc (4,5) = HH; còn TTT là bất khả vì 3 = H. Tương tự khi 1–3 = TTT, chỉ có 3–5 = TTT (4,5 = TT).
    + Do đó có đúng 2 chuỗi trong 2^5 = 32: HHHHH và TTTTT.
    + Vậy P(A∩B) = 2/32 = 1/16.
  - Suy ra P(A∪B) = 1/4 + 1/4 − 1/16 = 7/16.
- (c) Ít nhất 2 H trong (1–3) và ít nhất 2 T trong (3–5).
  - Xác suất ≥2 H trong 3 lần đầu = 1 − P(0 H) − P(1 H) = 1 − [C(3,0)+C(3,1)]/2^3 = 1 − (1+3)/8 = 1/2.
  - Xác suất ≥2 T trong 3 lần cuối = 1/2 (đối xứng).
  - Hai khối (1–3) và (3–5) không độc lập do cùng dùng lần 3, nên không thể nhân trực tiếp 1/2·1/2.
  - Ta dùng phân tích theo lần 3 (ký hiệu X3):
    + Nếu X3 = H (xác suất 1/2): điều kiện đầu cần ≥1 H trong (1,2) (vì đã có 1 H ở lần 3), xác suất = 1 − P(00) = 3/4. Điều kiện cuối cần ≥2 T trong (4,5), xác suất = C(2,2)/2^2 = 1/4. Độc lập theo các cặp (1,2) và (4,5) ⇒ P = (3/4)(1/4) = 3/16.
    + Nếu X3 = T (xác suất 1/2): điều kiện đầu cần ≥2 H trong (1,2), xác suất = 1/4; điều kiện cuối cần ≥1 T trong (4,5) (vì đã có 1 T ở lần 3), xác suất = 1 − P(11) = 3/4 ⇒ P = (1/4)(3/4) = 3/16.
  - Tổng: P = (1/2)(3/16) + (1/2)(3/16) = 3/16.

  # Ex40: Suppose that n independent trials, each of which results in any of the outcomes 0, 1, or 2, with respective probabilities .3, .5, and .2, are performed. Find the probability that both outcome 1 and outcome 2 occur at least once. (Hint: Consider the complementary probability.)
  ## Dịch sang tiếng Việt
  Giả sử thực hiện n phép thử độc lập, mỗi phép thử cho một trong ba kết quả 0, 1, 2 với xác suất lần lượt 0.3, 0.5, 0.2. Hãy tìm xác suất sao cho cả kết quả 1 và kết quả 2 đều xuất hiện ít nhất một lần. (Gợi ý: xét xác suất bù.)
  ## Giải
  - Gọi A: “không có 1 xuất hiện trong n lần”, B: “không có 2 xuất hiện trong n lần”. Ta cần P(A^c ∩ B^c) = 1 − P(A ∪ B).
  - Vì các lần độc lập và phân phối như nhau:
    - P(A) = P(mỗi lần ≠1)^n = (0.3 + 0.2)^n = 0.5^n.
    - P(B) = P(mỗi lần ≠2)^n = (0.3 + 0.5)^n = 0.8^n.
    - P(A ∩ B) = P(không có 1 và không có 2) = P(chỉ toàn 0)^n = 0.3^n.
  - Do đó, P(“có ≥1 lần ra 1 và ≥1 lần ra 2”) = 1 − [P(A) + P(B) − P(A ∩ B)] = 1 − (0.5^n + 0.8^n − 0.3^n).

  # Ex41: A parallel system functions whenever at least one of its components works. Consider a parallel system of n components, and suppose that each component independently works with probability 1/2. Find the conditional probability that component 1 works, given that the system is functioning.
  ## Dịch sang tiếng Việt
  Một hệ thống song song hoạt động khi ít nhất một linh kiện hoạt động. Xét hệ gồm n linh kiện, mỗi linh kiện hoạt động độc lập với xác suất 1/2. Hãy tìm xác suất có điều kiện rằng linh kiện 1 hoạt động, biết rằng hệ đang hoạt động.
  ## Giải
  - Ký hiệu X_i = 1 nếu linh kiện i hoạt động. Sự kiện hệ hoạt động S = {ít nhất một X_i = 1}.
  - Ta cần P(X_1=1 | S) = P(X_1=1 ∩ S)/P(S). Vì X_1=1 ⇒ S, nên P(X_1=1 ∩ S) = P(X_1=1) = 1/2.
  - P(S) = 1 − P(tất cả hỏng) = 1 − (1/2)^n.
  - Do đó P(X_1=1 | S) = (1/2) / (1 − 2^{-n}) = 2^{n-1} / (2^n − 1).

  # Ex42: A certain organism possesses a pair of each of 5 different genes (A, B, C, D, E). Each gene appears in 2 forms (lowercase and capital), with the capital letter dominant. In a mating between organisms having genotypes aA, bB, cC, dD, eE and aa, bB, cc, Dd, ee, what is the probability that the progeny will (1) phenotypically, (2) genotypically resemble (a) the first parent; (b) the second parent; (c) either parent; (d) neither parent?
  ## Dịch sang tiếng Việt
  Một sinh vật có 5 cặp gen khác nhau (A, B, C, D, E). Mỗi gen có 2 dạng (chữ thường và chữ hoa), và chữ hoa trội. Trong một phép lai giữa hai cơ thể có kiểu gen lần lượt aA, bB, cC, dD, eE và aa, bB, cc, Dd, ee, hãy tính xác suất đời con sẽ (1) giống bố/mẹ về kiểu hình, (2) giống về kiểu gen đối với: (a) bố/mẹ thứ nhất; (b) bố/mẹ thứ hai; (c) một trong hai; (d) không giống ai.
  ## Giải
  - Độc lập theo từng locus (gen) và giữa hai bố mẹ. Xét từng gen rồi nhân xác suất.
  - Kiểu hình của chữ hoa (A,B,C,D,E) là trội; chữ thường (a,b,c,d,e) chỉ biểu hiện khi đồng hợp lặn.

  Phân tích theo từng gen:
  - A: P1 aA (dị hợp), P2 aa (đồng hợp lặn) ⇒ con: aa với 1/2, aA với 1/2. Kiểu hình: A với 1/2, a với 1/2.
  - B: P1 bB, P2 bB (cả hai dị hợp) ⇒ con: BB (1/4), bB (1/2), bb (1/4). Kiểu hình B với 3/4.
  - C: P1 cC, P2 cc ⇒ con: cc (1/2), cC (1/2). Kiểu hình: C 1/2, c 1/2.
  - D: P1 dD, P2 Dd ⇒ con: DD (1/4), Dd (1/2), dd (1/4). Kiểu hình D 3/4.
  - E: P1 eE, P2 ee ⇒ con: ee (1/2), eE (1/2). Kiểu hình: E 1/2, e 1/2.

  Kiểu hình của bố mẹ:
  - P1: A, B, C, D, E (dị hợp tất cả ⇒ đều biểu hiện trội).
  - P2: a, B, c, D, e (lặn ở A, C, E; trội ở B, D).

  1) Xác suất giống về kiểu hình (toàn bộ 5 gen):
  - Giống P1: (1/2)·(3/4)·(1/2)·(3/4)·(1/2) = (1/2)^3 (3/4)^2 = 9/128.
  - Giống P2: (1/2)·(3/4)·(1/2)·(3/4)·(1/2) = 9/128.
  - Hai sự kiện trên loại trừ nhau (khác nhau ở A, C, E) ⇒ Giống một trong hai = 9/128 + 9/128 = 9/64.
  - Không giống ai (về kiểu hình) = 1 − 9/64 = 55/64.

  2) Xác suất giống về kiểu gen (toàn bộ 5 gen):
  - Giống P1 (aA, bB, cC, dD, eE): mỗi locus trùng với P1 với xác suất 1/2 ⇒ (1/2)^5 = 1/32.
  - Giống P2 (aa, bB, cc, Dd, ee): mỗi locus trùng với P2 với xác suất 1/2 ⇒ (1/2)^5 = 1/32.
  - Hai sự kiện trên loại trừ nhau ⇒ Giống một trong hai = 1/32 + 1/32 = 1/16.
  - Không giống ai (về kiểu gen) = 1 − 1/16 = 15/16.

# Ex43: Three prisoners A, B, and C are in jail. Exactly one of them will be pardoned and the other two will be executed. Prisoner A asks the jailer to name one (but not A) who will be executed. The jailer says “B will be executed.” What is the probability that A will be executed? Explain why the answer depends on the jailer’s disclosure policy, and compute it under the policy that whenever both B and C will be executed the jailer chooses uniformly at random which name to say.
## Dịch sang tiếng Việt
Ba tù nhân A, B, C đang ở tù. Chỉ có đúng một người sẽ được ân xá, hai người còn lại sẽ bị xử tử. Tù nhân A yêu cầu cai ngục nêu tên một người (không phải A) sẽ bị xử tử. Cai ngục nói “B sẽ bị xử tử.” Hỏi xác suất A sẽ bị xử tử là bao nhiêu? Giải thích vì sao đáp án phụ thuộc vào cách cai ngục chọn tên để tiết lộ, và hãy tính theo chính sách: nếu cả B và C đều sẽ bị xử tử thì cai ngục chọn ngẫu nhiên đều giữa hai tên để nói.
## Giải
- Các trường hợp ân xá (mỗi trường hợp xác suất 1/3): (i) ân xá A ⇒ B, C bị xử; (ii) ân xá B ⇒ A, C bị xử; (iii) ân xá C ⇒ A, B bị xử.
- Chính sách tiết lộ: nếu ân xá A thì có thể nói “B” hoặc “C” với xác suất 1/2; nếu ân xá B thì buộc phải nói “C”; nếu ân xá C thì buộc phải nói “B”.
- Sự kiện nghe “B” xảy ra trong hai tình huống: ân xá A (với xác suất có điều kiện 1/2) hoặc ân xá C (xác suất 1). Do đó
  P(nghe “B”) = (1/3)·(1/2) + (1/3)·1 = 1/6 + 1/3 = 1/2.
- A bị xử tử khi và chỉ khi người được ân xá là B hoặc C. Trong điều kiện đã nghe “B”, chỉ tình huống ân xá C là phù hợp (ân xá A thì A không bị xử). Vậy
  P(A bị xử | nghe “B”) = P(ân xá C | nghe “B”) = [(1/3)·1] / [1/2] = 2/3.
- Nhận xét: Nếu chính sách tiết lộ khác (ví dụ luôn ưu tiên nói “B” khi có thể), hậu nghiệm có thể khác. Vì vậy cần chỉ rõ chính sách tiết lộ; với chính sách đồng đều ở trên, xác suất A bị xử vẫn là 2/3 (không đổi so với tiên nghiệm).

# Ex44: Eye color is determined by a single gene with two alleles: B (brown, dominant) and b (blue, recessive). If both parents are brown-eyed heterozygotes (genotype Bb × Bb), what is the probability that their child has blue eyes?
## Dịch sang tiếng Việt
Màu mắt do một gen với hai alen quyết định: B (nâu, trội) và b (xanh, lặn). Nếu cả hai cha mẹ đều mắt nâu dị hợp (kiểu gen Bb × Bb), xác suất con sinh ra có mắt xanh là bao nhiêu?
## Giải
- Lập bảng Punnett cho Bb × Bb:
  - BB (1/4), Bb (1/2), bb (1/4).
- Kiểu hình mắt xanh chỉ khi đồng hợp lặn bb. Do đó P(mắt xanh) = 1/4.
- Ghi chú: Nếu chỉ biết “mắt nâu” mà không biết kiểu gen (BB hay Bb), cần thêm thông tin về tần suất alen trong quần thể mới suy ra được xác suất bb của con.

# Ex45: Two teams, A and B, play a best-of-7 series (first to 4 wins). Each game is won by team A with probability p, independently of other games. Answer the following:
(a) Given that after 3 games one of the teams leads 3–0, what is the conditional probability that it is team A who leads?
(b) Given that after 3 games one of the teams leads 3–0, what is the probability that team A will ultimately win the series?
(c) For the fair case p = 1/2, what is the probability that the team that eventually wins the series also won Game 1?
## Dịch sang tiếng Việt
Hai đội A và B chơi loạt tối đa 7 trận (đội nào đạt 4 thắng trước thì vô địch). Mỗi trận A thắng với xác suất p, độc lập giữa các trận. Hãy trả lời:
(a) Biết rằng sau 3 trận có một đội dẫn 3–0, xác suất đội đang dẫn là A bằng bao nhiêu?
(b) Biết rằng sau 3 trận có một đội dẫn 3–0, xác suất đội A sẽ vô địch cả loạt bằng bao nhiêu?
(c) Trường hợp công bằng p = 1/2, xác suất đội vô địch cả loạt đồng thời đã thắng Trận 1 là bao nhiêu?
## Giải
- (a) Xác suất A dẫn 3–0 là p^3; B dẫn 3–0 là (1−p)^3. Có điều kiện “một đội đang dẫn 3–0”, xác suất đội dẫn là A bằng
  P(A dẫn 3–0 | có đội dẫn 3–0) = p^3 / (p^3 + (1−p)^3).
- (b) Nếu A đang dẫn 3–0 thì A vô địch với xác suất 1 − (1−p)^4 (chỉ thua cả 4 trận còn lại mới mất chức). Nếu B đang dẫn 3–0 thì để A vô địch cần A thắng cả 4 trận kế tiếp: xác suất p^4. Dùng (a) để trộn theo xác suất đội đang dẫn:
  P(A vô địch | có đội dẫn 3–0)
  = [p^3/(p^3+(1−p)^3)] · [1 − (1−p)^4] + [(1−p)^3/(p^3+(1−p)^3)] · p^4.
- (c) Xác suất đội vô địch đã thắng Trận 1 (trường hợp p=1/2). Do tính đối xứng, “đội vô địch” có thể là A hoặc B. Đếm theo độ dài loạt (4, 5, 6, 7 trận), và yêu cầu “vô địch” thắng trận cuối cùng và cũng thắng Trận 1:
  - Kết thúc sau 4 trận: chỉ có chuỗi WWWW cho đội vô địch; xác suất cho một đội là (1/2)^4, cho hai đội là 2·(1/2)^4 = 1/8.
  - Sau 5 trận: với đội vô địch, trong 4 trận đầu phải có đúng 3 thắng và Trận 1 là thắng ⇒ có C(3,2)=3 chuỗi hợp lệ; nhân cho hai đội: 2·3·(1/2)^5 = 3/16.
  - Sau 6 trận: trong 5 trận đầu có đúng 3 thắng và Trận 1 thắng ⇒ C(4,2)=6; cho hai đội: 2·6·(1/2)^6 = 3/16.
  - Sau 7 trận: trong 6 trận đầu có đúng 3 thắng và Trận 1 thắng ⇒ C(5,2)=10; cho hai đội: 2·10·(1/2)^7 = 5/32.
  Cộng lại: 1/8 + 3/16 + 3/16 + 5/32 = 21/32.
  Vậy trong loạt công bằng, xác suất đội vô địch cũng thắng Trận 1 là 21/32.

# Ex46: Suppose that distinct integer values are written on each of 3 cards. You will be offered these cards in a random order. When you are offered a card you must immediately either accept it or reject it. If you accept a card, the process ends. If you reject a card, then the next card (if a card remains) is offered. If you reject the first two cards offered, then you must accept the final card.
(a) If you plan to accept the first card offered, what is the probability that you will accept the highest valued card?
(b) If you plan to reject the first card offered, and to then accept the second card if and only if its value is greater than the value of the first card, what is the probability that you will accept the highest valued card?
## Dịch sang tiếng Việt
Giả sử có 3 thẻ, mỗi thẻ mang một giá trị nguyên khác nhau. Bạn sẽ được đưa các thẻ theo thứ tự ngẫu nhiên. Mỗi khi được đưa một thẻ, bạn phải ngay lập tức chấp nhận hoặc từ chối. Nếu chấp nhận thì dừng; nếu từ chối thì tiếp tục sang thẻ kế tiếp (nếu còn). Nếu bạn từ chối hai thẻ đầu tiên, bạn buộc phải nhận thẻ cuối cùng.
(a) Nếu bạn dự định nhận thẻ đầu tiên, xác suất bạn nhận được thẻ có giá trị lớn nhất là bao nhiêu?
(b) Nếu bạn dự định từ chối thẻ đầu tiên, và chỉ nhận thẻ thứ hai nếu giá trị của nó lớn hơn giá trị của thẻ thứ nhất, thì xác suất bạn nhận được thẻ có giá trị lớn nhất là bao nhiêu?
## Giải
- Ký hiệu thứ hạng (cao nhất H, trung bình M, thấp nhất L); các thứ tự xuất hiện đều nhau (6 hoán vị).
- (a) Nhận thẻ đầu tiên ⇒ nhận H khi và chỉ khi thẻ đầu tiên là H. Xác suất = 1/3.
- (b) Chiến lược: bỏ thẻ 1; nhận thẻ 2 nếu và chỉ nếu nó cao hơn thẻ 1; nếu không thì nhận thẻ 3.
  - Nếu thẻ 1 = H: thẻ 2 không thể cao hơn ⇒ nhận thẻ 3 (không phải H) ⇒ thất bại. Có 2 hoán vị bắt đầu bằng H: HML, HLM ⇒ đều thất bại.
  - Nếu thẻ 1 = M: thẻ 2 là H thì nhận H (thắng); thẻ 2 = L thì từ chối và nhận thẻ 3 = H (thắng). Hai hoán vị MHL, MLH ⇒ đều thắng.
  - Nếu thẻ 1 = L: nhận thẻ 2 (vì luôn cao hơn L); chỉ thắng nếu thẻ 2 = H. Trong hai hoán vị LHM, LMH ⇒ chỉ LHM thắng.
  - Tổng kết: 3/6 hoán vị thắng ⇒ xác suất = 1/2.

# Ex47: Let A, B, C be events such that P(A) = 0.2, P(B) = 0.3, P(C) = 0.4. Find the probability that at least one of the events A and B occurs if (a) A and B are mutually exclusive; (b) A and B are independent. Find the probability that all of the events A, B, C occur if (c) A, B, C are independent; (d) A, B, C are mutually exclusive.
## Dịch sang tiếng Việt
Cho các biến cố A, B, C với P(A) = 0.2, P(B) = 0.3, P(C) = 0.4. Hãy tìm xác suất “ít nhất một trong A, B xảy ra” nếu (a) A, B xung khắc; (b) A, B độc lập. Tìm xác suất “cả A, B, C đều xảy ra” nếu (c) A, B, C độc lập; (d) A, B, C xung khắc.
## Giải
- (a) Xung khắc: P(A∪B) = P(A) + P(B) = 0.2 + 0.3 = 0.5.
- (b) Độc lập: P(A∪B) = P(A) + P(B) − P(AB) = 0.2 + 0.3 − (0.2)(0.3) = 0.44.
- (c) Độc lập ba biến: P(ABC) = P(A)P(B)P(C) = 0.2·0.3·0.4 = 0.024.
- (d) Xung khắc (không thể xảy ra đồng thời từng cặp) ⇒ không thể có cả ba cùng xảy ra ⇒ P(ABC) = 0.

# Ex48: Two percent of women of age 45 who participate in routine screening have breast cancer. Ninety percent of those with breast cancer have positive mammographies. Ten percent of the women who do not have breast cancer will also have positive mammographies. Given a woman has a positive mammography, what is the probability she has breast cancer?
## Dịch sang tiếng Việt
Hai phần trăm phụ nữ 45 tuổi tham gia sàng lọc định kỳ bị ung thư vú. 90% người bị ung thư vú có chụp nhũ ảnh dương tính. 10% người không bị ung thư vú cũng có dương tính. Biết một phụ nữ có nhũ ảnh dương tính, xác suất cô ấy bị ung thư vú là bao nhiêu?
## Giải
- Ký hiệu C: có ung thư; T: dương tính. Cho: P(C)=0.02; P(T|C)=0.90; P(T|C^c)=0.10.
- Bayes: P(C|T) = [P(T|C)P(C)] / [P(T|C)P(C) + P(T|C^c)P(C^c)]
  = (0.90·0.02) / (0.90·0.02 + 0.10·0.98)
  = 0.018 / (0.018 + 0.098)
  = 0.018 / 0.116 ≈ 0.1552 ≈ 15.5%.
- Nhận xét: Tỷ lệ dương giả cao làm cho xác suất hậu nghiệm không lớn dù test khá nhạy.

# Ex49: Twelve percent of all US households are in California. A total of 3.3 percent of all US households earn over 250,000 per year, while a total of 6.3 percent of California households earn over 250,000 per year. If a randomly chosen US household earns over 250,000 per year, what is the probability it is from California?
## Dịch sang tiếng Việt
12% hộ gia đình ở Mỹ thuộc California. Tổng cộng 3.3% hộ gia đình Mỹ thu nhập trên 250,000/năm, trong khi 6.3% hộ ở California có thu nhập trên 250,000/năm. Nếu chọn ngẫu nhiên một hộ gia đình Mỹ có thu nhập trên 250,000/năm, xác suất hộ đó ở California là bao nhiêu?
## Giải
- Ký hiệu CA: “ở California”; H: “thu nhập > 250k”. Cho: P(CA)=0.12; P(H)=0.033; P(H|CA)=0.063.
- Ta cần P(CA|H) = [P(H|CA)P(CA)] / P(H).
- Trước hết kiểm tra tính nhất quán: P(H) theo tổng xác suất = P(H|CA)P(CA) + P(H|CA^c)P(CA^c).
  - Suy ra P(H|CA^c) = [P(H) − P(H|CA)P(CA)] / (1 − P(CA)) = [0.033 − 0.063·0.12]/0.88 = (0.033 − 0.00756)/0.88 ≈ 0.02886 ≈ 2.886%.
- Nay Bayes: P(CA|H) = (0.063·0.12)/0.033 = 0.00756 / 0.033 ≈ 0.2291 ≈ 22.9%.

# Ex50: There is a 60 percent chance that the event A will occur. If A does not occur, there is a 10 percent chance that B will occur. What is the probability that at least one of the events A or B occur?
## Dịch sang tiếng Việt
Có 60% khả năng biến cố A xảy ra. Nếu A không xảy ra, có 10% khả năng biến cố B xảy ra. Xác suất để ít nhất một trong hai biến cố A hoặc B xảy ra là bao nhiêu?
## Giải
- Cho: P(A)=0.6; P(B|A^c)=0.1.
- Xác suất “A hoặc B” = P(A) + P(B∩A^c) = 0.6 + 0.1·P(A^c) = 0.6 + 0.1·0.4 = 0.64.

# Ex51: Suppose distinct values are written on each of three cards, which are then randomly given the designations A, B, and C. The values on cards A and B are then compared. What is the probability that the smaller of these values is also smaller than the value on card C?
## Dịch sang tiếng Việt
Giả sử các giá trị khác nhau được viết trên 3 thẻ, rồi ngẫu nhiên gán ký hiệu A, B, C. So sánh giá trị trên A và B. Xác suất giá trị nhỏ hơn trong hai giá trị này cũng nhỏ hơn giá trị trên thẻ C là bao nhiêu?
## Giải
- Gọi thứ hạng của (A,B,C) là hoán vị của {1,2,3} với 1 nhỏ nhất, 3 lớn nhất; có 6 hoán vị đều nhau.
- Ta cần P(min{A,B} < C). Chỉ thất bại khi C là nhỏ nhất (hạng 1), vì khi đó min{A,B} = 2 > C.
- Xác suất C là nhỏ nhất = 1/3. Do đó P(thành công) = 1 − 1/3 = 2/3.
- Đây là kết quả đã xuất hiện (Ex20) dưới dạng khác; kết quả là 2/3.