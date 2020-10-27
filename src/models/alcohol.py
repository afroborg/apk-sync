import mongoengine


class Alcohol(mongoengine.Document):
    productId: str = mongoengine.StringField(required=True)
    productNumber: str = mongoengine.StringField(required=True)
    productName: str = mongoengine.StringField(required=True)
    brand: str = mongoengine.StringField()
    categories: list = mongoengine.ListField()
    image: str = mongoengine.StringField()
    available: bool = mongoengine.BooleanField(default=True)
    percentage: float = mongoengine.FloatField(min_value=0)
    volume: float = mongoengine.FloatField(min_value=0)
    price: float = mongoengine.FloatField(min_value=0)
    apk: float = mongoengine.FloatField(min_value=0)

    meta = {
        'db_alias': 'APK',
        'collection': 'alcohols'
    }

    def __init__(self, systembolaget_data, *args, **kwargs):
        super(mongoengine.Document, self).__init__(*args, **kwargs)
        self.productId = systembolaget_data['productId']
        self.productNumber = systembolaget_data['productNumber']
        self.productName = self._generate_name(
            systembolaget_data['productNameBold'], systembolaget_data['productNameThin'])
        self.brand = systembolaget_data['producerName']
        self.categories = list([
            systembolaget_data['categoryLevel1'],
            systembolaget_data['categoryLevel2'],
            systembolaget_data['categoryLevel3'],
            systembolaget_data['categoryLevel4'],

        ])
        self.image = self._get_image(systembolaget_data['images'])
        self.available = not systembolaget_data['isDiscontinued']
        self.percentage = systembolaget_data['alcoholPercentage']
        self.volume = systembolaget_data['volume']
        self.price = systembolaget_data['price']

        self.apk = self._calculate_apk()

    def _generate_name(self, bold: str, thin: str) -> str:
        return bold + ' ' + thin if thin else bold

    def _get_image(self, images: list) -> str:
        if(images != None and len(images) > 0):
            return str(images[0]['imageUrl']) + '_400.png'

        return None

    # This is where the magic happens :)
    def _calculate_apk(self) -> float:
        return (self.percentage / 100) * self.volume / self.price
