from facades import facade_c
from facade_7 import facade_7
from facade_v import facade_v
from facade_a import facade_a
from facade_9 import facade_9
from facade_entrance_group_lk import facade_entrance_group_lk
from ceiling_pc import ceiling_pc
from ceiling_in import ceiling_in
from ceiling_bc import ceiling_bc
from ceiling_v1v import ceiling_v1v
from gallery_g import gallery_g
from gallery_n import gallery_n
from gallery_ceiling import ceiling_gallery
from the_object import TheObject

novoros = TheObject(
    facade_7,
    facade_9,
    facade_c,
    facade_a,
    facade_v,
    facade_entrance_group_lk,
    ceiling_pc,
    ceiling_in,
    ceiling_bc,
    ceiling_v1v,
    gallery_g,
    gallery_n,
    ceiling_gallery,
)


# print(novoros.get_list_cassette_by_ral_or_size(filename="data/ral9003.xlsx", ral=9003))
# print(novoros.get_list_cassette_by_ral_or_size(filename="data/2023-07-11_Список_кассет.xlsx", ral=9006))

print(f"RAL9006: {novoros.square(ral=9006)}m2")
print(f"RAL9003: {novoros.square(ral=9003)}m2")
