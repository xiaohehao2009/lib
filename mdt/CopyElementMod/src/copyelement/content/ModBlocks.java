package copyelement.content;

import mindustry.content.Items;
import mindustry.type.Category;
import mindustry.world.Block;
import static mindustry.type.ItemStack.with;

public class ModBlocks {
    public static Block copyElement;

    public void load() {
        copyElement = new CopyElement("copy-element") {{
            requirements(Category.distribution, with(Items.copper, 4, Items.lead, 2));
            buildCostMultiplier = 2f;
        }};
    }
}
