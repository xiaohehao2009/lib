package fastbuild;

import mindustry.mod.Mod;
import mindustry.Vars;
import mindustry.world.blocks.storage.CoreBlock;

public class FastBuildMod extends Mod {
    @Override
    public void loadContent() {
        Vars.content.each(content -> {
            if (content instanceof CoreBlock core) {
                core.unitType.buildSpeed *= 10f;
            }
        });
    }
}
