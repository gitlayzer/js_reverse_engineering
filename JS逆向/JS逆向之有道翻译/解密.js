const crypto = require('crypto');

function y(e) {
                return crypto.createHash("md5").update(e).digest()
            }

function decrypt(t) {
                if (!t)
                    return null;
                // e.alloc ，e其实是内置的Buffer对象，可以替换成Buffer
                // o和n可以在浏览器断点调试中获取固定值
                let o = 'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'
                let n = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'
                const a = Buffer.alloc(16, y(o)) //a = e.alloc(16, y(o))
                  , i = Buffer.alloc(16, y(n)) // i = e.alloc(16, y(n))
                    // c.a.createDecipheriv 其实是加密算法crypto.createDecipheriv， c.a可以替换成crypto，需要额外导入
                  , r = crypto.createDecipheriv("aes-128-cbc", a, i);
                let s = r.update(t, "base64", "utf-8");
                return s += r.final("utf-8")
}
// var encrypt_data = "Z21kD9ZK1ke6ugku2ccWu-MeDWh3z252xRTQv-wZ6jddVo3tJLe7gIXz4PyxGl73nSfLAADyElSjjvrYdCvEP4pfohVVEX1DxoI0yhm36ytQNvu-WLU94qULZQ72aml6JKK7ArS9fJXAcsG7ufBIE0gd6fbnhFcsGmdXspZe-8whVFbRB_8Fc9JlMHh8DDXnskDhGfEscN_rfi-A-AHB3F9Vets82vIYpkGNaJOft_JA-m5cGEjo-UNRDDpkTz_NIAvo5PbATpkh7PSna2tHcE6Hou9GBtPLB67vjScwplB96-zqZKXJJEzU5HGF0oPDY_weAkXArzXyGLBPXFCnn_IWJDkGD4vqBQQAh2n52f48GD_cb-PSCT_8b-ESsKUI9NJa11XsdaUZxAc8TzrYnXwdcQbtl_kZGKhS6_rCtuNEBouA_lvM2CbS7TTtV2U4zVmJKpp-c6nt3yZePK3Av01GWn1pH_3sZbaPEx8DUjSbdp4i4iK-Mj4p2HPoph67DR7B9MFETYku_28SgP9xsKRRvFH4aHBHESWX4FDbwaU="
// console.log(decrypt(encrypt_data))
//{"code":0,"dictResult":{"ec":{"exam_type":["初中","高中","CET4","CET6","考研"],"word":{"usphone":"ˈæp(ə)l","ukphone":"ˈæp(ə)l","ukspeech":"apple&type=1","trs":[{"pos":"n.","tran":"苹果"}],"wfs":[{"wf":{"name":"复数","value":"apples"}}],"return-phrase":"apple","usspeech":"apple&type=2"}}},"translateResult":[[{"tgt":"苹果","src":"apple","tgtPronounce":"pín guŏtype":"en2zh-CHS"}