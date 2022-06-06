from pylabview_helpers.vi import get_vi
from pylabview import LVheap


def get_text_from_heap(heap, encoding="cp1252"):
    plaintext = ""
    for i, heap_object in enumerate(heap):
        tagName = LVheap.tagEnToName(heap_object.tagEn, heap_object.parent)
        if "text" == tagName:
            try:
                plaintext += heap_object.content.decode(encoding) + "\n"
            except UnicodeDecodeError:
                raise RuntimeError("failed decode:" + str(heap_object.content))
        if "ConstValue" == tagName:
            # TODO, this works for string constants, but not other composite types that contain strings.
            # I'm going to have to actually handle the type recursively to get those working
            for child in heap_object.parent.childs:
                childTagName = LVheap.tagEnToName(child.tagEn, child.parent)
                if childTagName == "ddo":
                    if (
                        LVheap.SL_SYSTEM_ATTRIB_TAGS.SL__class.value in child.attribs
                        and child.attribs[LVheap.SL_SYSTEM_ATTRIB_TAGS.SL__class.value]
                        == LVheap.SL_CLASS_TAGS.SL__stdString
                    ):
                        plaintext += heap_object.content[4:].decode(encoding) + "\n"
                        break
    return plaintext


def get_vi_plaintext(path):
    plaintext = ""
    vi = get_vi(path)
    # TODO see what else shows up in the main XML and parse that
    # root = vi.exportXMLRoot()
    for block in vi.blocks.values():
        for section_num, section in block.sections.items():
            root = section
            parent_elems = []
            elem = None
            if getattr(section, "objects", None):
                plaintext += get_text_from_heap(section.objects)

    return plaintext
