from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app import db  

class WarehouseItems(db.Model):
    __tablename__ = 'Warehouse_Items'
    __table_args__ = {'schema': 'dbo'}

    id = db.Column(db.Integer, primary_key=True)
    warehouse_info_id = db.Column(db.Integer, db.ForeignKey('dbo.Warehouse_Info.Warehouse_Info_Id'), nullable=False)
    Item_Name = db.Column(db.String, nullable=False)
    Item_Unit_Quant = db.Column(db.Float, nullable=False)
    Item_Capacity_Quant = db.Column(db.Float, nullable=False)
    Item_Space_Acquired = db.Column(db.Float)
    Item_Price_Per_Unit = db.Column(db.Float, nullable=False)
    Item_Total_Cost = db.Column(db.Float)

    warehouse_info = db.relationship("WarehouseInfo", back_populates="warehouse_items", overlaps="Warehouse_Info")

    def __repr__(self):
        return f"<WarehouseItem {self.Item_Name}, Quantity: {self.Item_Unit_Quant}>"
