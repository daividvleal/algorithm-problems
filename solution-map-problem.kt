interface Map{
    fun setAll(key: String, value: Int)
    fun set(key: String, value: Int)
    fun get(key: String): Int
}

class ContentMap: Map{

    // The main idea for this solution is to have a
    // HashMap to save only the cases that we need a
    // different value
    private var hashMap = HashMap<String, Int>()

    // We save a value for all the elements
    private var valueAll = 0

    /*
        When setAll reset the hashmap, because all the elements will have the same value
     */
    override fun setAll(key: String, value: Int) {
        this.hashMap = HashMap()
        this.valueAll = value
    }

    /*
        When set a new element we use the HashMap because we gonna need just O(1)
     */
    override fun set(key: String, value: Int) {
        hashMap[key] = value
    }

    /*
        When we try to retrieve an element, we just verify if it exists on the HashMap
        if true, retrieve the element
        else the default value
     */
    override fun get(key: String): Int {
        hashMap[key]?.let{
            return it
        } ?: run {
            return valueAll
        }
    }

}

fun main() {

    val contentMap = ContentMap()

    for (i in 0..1000000){
        contentMap.set("key$i", i)
    }

    //expect to key10000 be 10000
    print(contentMap.get("key10000"))
    print("\n")
    //expected all to be 50 after this
    contentMap.setAll("", 50)
    //expected key10000 to be 50
    print(contentMap.get("key10000"))
    print("\n")
    //expect to key9 be 9
    contentMap.set("key9", 9)
    print(contentMap.get("key9"))
    print("\n")
    //expect to key100 be 50
    print(contentMap.get(("key100")))
    
}
