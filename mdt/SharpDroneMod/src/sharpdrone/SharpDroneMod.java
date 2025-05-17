package sharpdrone;

import mindustry.mod.Mod;
import mindustry.Vars;
import mindustry.world.blocks.storage.CoreBlock;

public class SharpDroneMod extends Mod {
    @Override
    public void loadContent() {
        Vars.content.each(content -> {
            if (content instanceof CoreBlock core) {
                core.unitType.weapons.each(weapon -> {
                    weapon.bullet.buildingDamageMultiplier = 1f;
                    weapon.bullet.damage *= 100f;
                });
            }
        });
    }
}
