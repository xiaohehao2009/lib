using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CatchTheBeans
{
    internal abstract class Scene
    {
        public abstract void Start();
        public abstract void Update(Game game);
    }
}
