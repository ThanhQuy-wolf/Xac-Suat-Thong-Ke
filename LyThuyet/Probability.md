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
<!-- - (h) Nhiều nhất hai trong số chúng xảy ra: (E ∩ F ∩ G^c) ∪ (E ∩ F^c ∩ G) ∪ (E^c ∩ F ∩ G) ∪ (E^c ∩ F^c ∩ G^c)
- (i) Đúng hai trong số chúng xảy ra: (E ∩ F ∩ G^c) ∪ (E ∩ F^c ∩ G) ∪ (E^c ∩ F ∩ G) -->
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