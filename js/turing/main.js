import { readFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import Executer from './executer.js';

const dir = dirname(fileURLToPath(import.meta.url));
const source = readFileSync(join(dir, '/programs/target.tur')).toString();
Executer.runFromSource(source);
