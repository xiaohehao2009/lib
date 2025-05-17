package copyelement.content;

import mindustry.content.Items;
import mindustry.content.Blocks;
import mindustry.content.TechTree;
import mindustry.content.TechTree.TechNode;
import static mindustry.type.ItemStack.with;

public class ModTechTree {
    public void load() {
        new TechNode(TechTree.all.find(t -> t.content == Blocks.router), ModBlocks.copyElement, with(Items.copper, 50, Items.lead, 50));
    }
}
