src/Component/.../{CompCategory}/{CompName}.php

* `interface CompName extends ParentClass`
* any function not (identical) in parent class `public function withSomething(typehint param): CompName;` to be implemented (no content)

src/Component/.../{CompCategory}/Factory.php

* detailed documentation
* `public function compName(typehint param): CompName;` to be implemented (no content)

src/Implementation/Component/.../{CompCategory}/{CompName}.php

* actual function content for logic and processing

src/Implementation/Component/.../{CompCategory}/Factory.php

* actually creating the class object, implementing the factory

src/Implementation/Component/.../{CompCategory}/Renderer.php

* list switch case at top, pointing to function
* function to fill template


