// TypeScript - 2.4/ES6

export let var1Boolean: boolean = true;

export let var2Decimal: number = 13;
export let var3Hex: number = 0xf00d;
export let var4Binary: number = 0b111111;
export let var5Octal: number = 0o744;

export let var6String: string = 'Hello, world!';

export let var7Array: any[] = [1, 'test', {a: 3}, 4, 5];
export let var8NumericArray: number[] = [1, 2, 3, 4, 5];

export let var9Tuple: [string, number] = ['key', 12345];

export enum Color {Red = 1, Green = 2, Blue = 4};
export let var10Enum: Color = Color.Blue;

export let var11ArrayOfAny: Array<any> = [1, 'test', {a: 3}, 4, 5];

export function var12VoidFunction(): void {};

export let var13Null: null = null;
export let var14Undefined: undefined = undefined;

export function var15NeverFunction(): never {
    throw new Error('test');
};
